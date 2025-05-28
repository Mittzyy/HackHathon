# Arsitektur EduLocal AI

1. **User** mengirim pesan via WhatsApp ke nomor Twilio sandbox.
2. **Twilio** mem-forward request ke endpoint FastAPI `/whatsapp`.
3. **FastAPI**:
   - Panggil `translator.translate()`
   - Panggil `qa_engine.get_answer()`
   - Kembalikan TwiML message ke Twilio.
4. **Twilio** mengirim balasan ke user.