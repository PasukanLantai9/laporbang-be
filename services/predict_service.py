from utils.pothole_detector import detect_pothole

class PredictService:

    @staticmethod
    def predict_image(file):
        """
        Hanya prediksi gambar, tidak menyimpan file.
        """
        # Langsung kirim file ke detect_pothole
        result = detect_pothole(file)
        return result
