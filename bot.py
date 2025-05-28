# # src/bot.py

from fastapi import FastAPI, Form
from starlette.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse
from .chat_engine import get_response
from .admin import router as admin_router

app = FastAPI()
app.include_router(admin_router)

@app.post("/whatsapp")
async def whatsapp_reply(Body: str = Form(...), From: str = Form(...)):
    try:
        answer = get_response(Body)
        resp = MessagingResponse()
        resp.message(answer)
        return PlainTextResponse(str(resp), media_type="application/xml")
    except Exception as e:
        import logging
        logging.getLogger("uvicorn.error").exception("Error in /whatsapp:")
        return PlainTextResponse(f"Error: {e}", status_code=500)
