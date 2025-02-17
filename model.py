from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Load model and labels at module load
model = load_model("keras_model.h5", compile=False)
class_names = [line.strip() for line in open("labels.txt")]

def predict_image(image_path: str):
    """
    Given a local image path, returns (class_name, confidence).
    """
    # e.g. load and preprocess
    image = Image.open(image_path).convert("RGB")
    image = ImageOps.fit(image, (224,224), Image.Resampling.LANCZOS)
    x = np.asarray(image, dtype=np.float32)
    x = (x / 127.5) - 1
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    idx = np.argmax(preds)
    return class_names[idx], float(preds[0][idx])
