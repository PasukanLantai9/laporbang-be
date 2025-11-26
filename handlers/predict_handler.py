from fastapi import APIRouter, UploadFile, File
from services.predict_service import PredictService
from schemas.predict_schema import PredictResponse

router = APIRouter(
    prefix="/predict",
    tags=["Predict"]
)

@router.post("", response_model=PredictResponse)
async def predict_pothole(image: UploadFile = File(...)):
    return PredictService.predict_image(image)
