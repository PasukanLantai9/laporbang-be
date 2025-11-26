from fastapi import FastAPI
from handlers.predict_handler import router as predict_router

app = FastAPI(
    title="Pothole Detection API",
    version="1.0.0"
)

app.include_router(predict_router)

@app.get("/")
def root():
    return {"message": "Pothole Detection API is running!"}
