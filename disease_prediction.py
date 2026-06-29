import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

MODEL_PATH = "artifacts/crop_disease_model.keras"
IMAGE_SIZE = (224, 224)

CLASS_NAMES = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy"
]

def print_header():
    print("=" * 60)
    print("AGRISENSE - DISEASE PREDICTION MODULE")
    print("=" * 60)

def validate_image_path(image_path):
    if not os.path.exists(image_path):
        print("[ERROR] Image not found.")
        return False
    if not image_path.lower().endswith((".jpg", ".jpeg", ".png")):
        print("[ERROR] Unsupported image format.")
        return False
    return True

def load_prediction_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")
    model = tf.keras.models.load_model(MODEL_PATH)
    print("[SUCCESS] Trained Model Loaded Successfully")
    return model

def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=IMAGE_SIZE)
    img_array = image.img_to_array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_disease(model, processed_image):
    prediction = model.predict(processed_image, verbose=0)
    index = int(np.argmax(prediction))
    confidence = float(np.max(prediction)) * 100
    return CLASS_NAMES[index], confidence

def display_prediction_result(disease, confidence):
    print("\n" + "=" * 60)
    print("PREDICTION RESULT")
    print("=" * 60)
    print(f"Predicted Disease : {disease}")
    print(f"Confidence         : {confidence:.2f}%")
    print("=" * 60)

def main():
    print_header()
    image_path = input("\nEnter image path: ").strip()

    if not validate_image_path(image_path):
        return

    model = load_prediction_model()
    processed_image = preprocess_image(image_path)
    disease, confidence = predict_disease(model, processed_image)
    display_prediction_result(disease, confidence)

if __name__ == "__main__":
    main()