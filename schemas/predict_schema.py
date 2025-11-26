from pydantic import BaseModel
from typing import Optional

# -----------------------------
# REQUEST (optional metadata)
# -----------------------------
class PredictRequest(BaseModel):
    filename: Optional[str] = None
    content_type: Optional[str] = None


# -----------------------------
# HASIL JSON dari Gemini
# -----------------------------
class GeminiPotholeResult(BaseModel):
    ada_pothole: bool
    jumlah_pothole: int
    deskripsi: str


# -----------------------------
# RESPONSE API
# -----------------------------
class PredictResponse(BaseModel):
    model: str
    result: GeminiPotholeResult
