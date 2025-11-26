import google.generativeai as genai
from PIL import Image
import json
import requests
import io
from typing import Union

genai.configure(api_key="YOUR_API_KEY_HERE")

def load_image(input_image) -> Image.Image:
    """
    Helper: menerima berbagai jenis input image dan return PIL.Image
    """
    # Jika input berupa UploadFile (FastAPI)
    if hasattr(input_image, "file"):
        return Image.open(input_image.file)

    # Jika input berupa PIL Image
    if isinstance(input_image, Image.Image):
        return input_image

    # Jika input berupa bytes
    if isinstance(input_image, (bytes, bytearray)):
        return Image.open(io.BytesIO(input_image))

    # Jika input berupa URL
    if isinstance(input_image, str) and input_image.startswith("http"):
        resp = requests.get(input_image)
        return Image.open(io.BytesIO(resp.content))

    # Jika input berupa path string
    if isinstance(input_image, str):
        return Image.open(input_image)

    raise ValueError("Unsupported image input type")


def detect_pothole(input_image: Union[str, bytes, Image.Image]):
    """
    Deteksi pothole dari gambar (path, URL, bytes, UploadFile, atau PIL image)
    """
    # Load image (universal loader)
    img = load_image(input_image)

    # Init model
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = """
    Analisis gambar ini dan jawab dalam format JSON:
    {
        "ada_pothole": true/false,
        "jumlah_pothole": angka,
        "deskripsi": "penjelasan singkat"
    }

    Hanya berikan JSON tanpa text tambahan.
    """

    # Kirim image langsung tanpa harus simpan ke disk
    response = model.generate_content([prompt, img])
    text = response.text.strip()

    try:
        # Bersihkan JSON dari formatting
        if text.startswith("```json"):
            text = text.replace("```json", "")
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]

        return json.loads(text)

    except Exception:
        return {
            "ada_pothole": False,
            "jumlah_pothole": 0,
            "deskripsi": "Error parsing response",
            "raw_response": response.text
        }
