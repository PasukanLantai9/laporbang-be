from fastapi import APIRouter, UploadFile, File
from services.predict_service import PredictService

router = APIRouter(
    prefix="/predict",
    tags=["Predict"]
)

@router.post("")
async def predict_pothole(image: UploadFile = File(...)):
    """
    Endpoint untuk prediksi pothole dari gambar.
    """
    result = PredictService.predict_image(image)
    return result
