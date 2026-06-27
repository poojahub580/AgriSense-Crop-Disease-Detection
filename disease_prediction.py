import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

MODEL_PATH = "artifacts/crop_disease_model.h5"
IMAGE_SIZE = (224, 224)


def print_header():
    print("=" * 60)
    print("AGRISENSE - DISEASE PREDICTION MODULE")
    print("=" * 60)


def validate_image_path(image_path):
    if not os.path.exists(image_path):
        print(f"[ERROR] Image not found: {image_path}")
        return False

    valid_extensions = (".jpg", ".jpeg", ".png")

    if not image_path.lower().endswith(valid_extensions):
        print("[ERROR] Unsupported image format")
        return False

    return True


def load_prediction_model():
    if not os.path.exists(MODEL_PATH):
        print("[WARNING] Trained model not available")
        print("[INFO] Prediction module running in demo mode")
        return None

    model = tf.keras.models.load_model(MODEL_PATH)

    print("[SUCCESS] Model loaded successfully")

    return model


def preprocess_image(image_path):

    img = image.load_img(
        image_path,
        target_size=IMAGE_SIZE
    )

    img_array = image.img_to_array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    return img_array


def predict_disease(model, processed_image):

    if model is None:

        print(
            "[INFO] No trained model found."
        )

        print(
            "[INFO] Returning demo prediction."
        )

        return "Tomato___Healthy"

    prediction = model.predict(
        processed_image
    )

    predicted_class = np.argmax(
        prediction
    )

    return predicted_class


def display_prediction_result(result):

    print("\n" + "=" * 60)

    print("PREDICTION RESULT")

    print("=" * 60)

    print(f"Predicted Disease: {result}")

    print("=" * 60)


def main():

    print_header()

    image_path = input(
        "\nEnter image path: "
    ).strip()

    if not validate_image_path(
        image_path
    ):
        return

    model = load_prediction_model()

    processed_image = preprocess_image(
        image_path
    )

    result = predict_disease(
        model,
        processed_image
    )

    display_prediction_result(
        result
    )


if __name__ == "__main__":
    main()