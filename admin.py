# src/admin.py

from fastapi import APIRouter, HTTPException, Body
from .chat_engine import trainer

router = APIRouter(prefix="/admin", tags=["admin"])

@router.post("/train")
async def train_faq(pairs: list[list[str]] = Body(...)):
    """
    Retrain ChatBot on a JSON list of [ [q1,a1], [q2,a2], ... ].
    """
    try:
        flat = [item for pair in pairs for item in pair]
        trainer.train(flat)
        return {"status": "ok", "trained_pairs": len(pairs)}
    except Exception as e:
        raise HTTPException(500, f"Training failed: {e}")
