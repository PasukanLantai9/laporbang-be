from utils.pothole_detector import detect_pothole
from schemas.predict_schema import PredictResponse, GeminiPotholeResult
from config import GEMINI_MODEL


class PredictService:

    @staticmethod
    def predict_image(file):
        gemini_raw = detect_pothole(file)

        result = GeminiPotholeResult(
            ada_pothole=gemini_raw.get("ada_pothole", False),
            jumlah_pothole=gemini_raw.get("jumlah_pothole", 0),
            deskripsi=gemini_raw.get("deskripsi", "")
        )

        return PredictResponse(
            model=GEMINI_MODEL,
            result=result
        )
