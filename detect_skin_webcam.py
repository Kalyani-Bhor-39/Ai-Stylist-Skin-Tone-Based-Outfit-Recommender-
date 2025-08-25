import os
import random

# Try importing heavy libs only when needed
try:
    import cv2
    import numpy as np
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing.image import img_to_array
    TF_AVAILABLE = True
except Exception as e:
    print("Optional libs unavailable (OpenCV/TensorFlow). detect_skin_webcam will use fallback. Error:", e)
    TF_AVAILABLE = False

_MODEL = None
_MODEL_PATH = os.path.join("model", "skin_tone_model.h5")
CLASSES = ["fair", "brown", "black"]

def _load_model_once():
    global _MODEL
    if _MODEL is None and TF_AVAILABLE and os.path.exists(_MODEL_PATH):
        try:
            _MODEL = load_model(_MODEL_PATH)
            print("Skin tone model loaded.")
        except Exception as e:
            print("Failed to load model:", e)
            _MODEL = None

def detect_skin_tone():
    """
    Returns one of CLASSES. If TensorFlow/OpenCV/model not available, returns random 'brown' by default.
    Designed so it only opens webcam when called (not at import).
    """
    # If TF/OpenCV available and model exists -> run webcam capture + predict
    _load_model_once()

    if TF_AVAILABLE and _MODEL is not None:
        cap = cv2.VideoCapture(0)  # on Windows try CAP_DSHOW
        if not cap or not cap.isOpened():
            print("Webcam not available, falling back to default skin tone.")
            return random.choice(CLASSES)

        print("Press 'q' in webcam window to capture a sample.")
        img = None
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Capture Skin - Press q to capture", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                try:
                    img = cv2.resize(frame, (150, 150))
                except Exception:
                    img = frame
                break

        cap.release()
        cv2.destroyAllWindows()

        if img is None:
            return random.choice(CLASSES)

        try:
            arr = img_to_array(img) / 255.0
            arr = np.expand_dims(arr, axis=0)
            preds = _MODEL.predict(arr)
            idx = int(preds.argmax(axis=1)[0])
            return CLASSES[idx]
        except Exception as e:
            print("Prediction failed, fallback. Error:", e)
            return random.choice(CLASSES)

    # Fallback (no TF/OpenCV/model)
    print("Using fallback skin tone (no model).")
    return "brown"  # choose a stable default so UI shows something
