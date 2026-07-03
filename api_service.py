import os
import numpy as np
import tensorflow as tf

from flask import (
    Flask,
    jsonify,
    request
)

from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input


print("=" * 60)
print("AGRISENSE - API SERVICE MODULE")
print("=" * 60)


# ==========================================================
# PROJECT CONFIGURATION
# ==========================================================

MODEL_PATH = "artifacts/crop_disease_model.keras"

IMAGE_SIZE = (224, 224)

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png"
}


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


# ==========================================================
# FLASK INITIALIZATION
# ==========================================================

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


if not os.path.exists(UPLOAD_FOLDER):

    os.makedirs(UPLOAD_FOLDER)

print("[SUCCESS] Upload Directory Ready")
# ==========================================================
# FILE VALIDATION
# ==========================================================
# Check whether the uploaded file has a valid image extension
def allowed_file(filename):

    if "." not in filename:
        return False

    extension = filename.rsplit(".", 1)[1].lower()

    return extension in ALLOWED_EXTENSIONS


# ==========================================================
# MODEL LOADING
# ==========================================================
# Load the trained crop disease prediction model
def load_prediction_model():

    if not os.path.exists(MODEL_PATH):

        print("[WARNING] Trained model not found.")
        print("[INFO] API will run in Demo Mode.")

        return None

    model = tf.keras.models.load_model(
        MODEL_PATH
    )

    print("[SUCCESS] Trained Model Loaded Successfully")

    return model


MODEL = load_prediction_model()


# ==========================================================
# IMAGE PREPROCESSING
# ==========================================================
# Preprocess the uploaded image before making predictions
def preprocess_image(image_path):

    img = image.load_img(
        image_path,
        target_size=IMAGE_SIZE
    )

    img_array = image.img_to_array(img)

    img_array = img_array.astype("float32")

    img_array = preprocess_input(img_array)

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    return img_array


# ==========================================================
# DISEASE PREDICTION
# ==========================================================
# Predict the crop disease using the trained model
def predict_disease(image_path):

    processed_image = preprocess_image(
        image_path
    )

    if MODEL is None:

        return {

            "status": "Demo Mode",

            "prediction": "Tomato_healthy",

            "confidence": "N/A"

        }

    prediction = MODEL.predict(

        processed_image,

        verbose=0

    )

    predicted_index = int(

        np.argmax(prediction)

    )

    confidence = float(

        np.max(prediction)

    ) * 100

    disease = CLASS_NAMES[
        predicted_index
    ]

    return {

        "status": "Prediction Completed",

        "prediction": disease,

        "confidence": round(
            confidence,
            2
        )

    }
# ==========================================================
# HOME ROUTE
# ==========================================================

@app.route("/")
def home():

    return jsonify({

        "project": "AgriSense Crop Disease Detection",

        "status": "API Running",

        "version": "1.0",

        "developer": "AgriSense"

    })


# ==========================================================
# HEALTH CHECK ROUTE
# ==========================================================

@app.route("/health")
def health():

    return jsonify({

        "server": "Online",

        "model_status":
            "Loaded"
            if MODEL is not None
            else
            "Demo Mode",

        "dataset_classes": len(CLASS_NAMES),

        "image_size": IMAGE_SIZE

    })


# ==========================================================
# DISEASE PREDICTION API
# ==========================================================

@app.route(
    "/predict",
    methods=["POST"]
)
def prediction_api():

    try:

        if "image" not in request.files:

            return jsonify({

                "success": False,

                "message": "Image file not found."

            }), 400

        uploaded_image = request.files["image"]

        if uploaded_image.filename == "":

            return jsonify({

                "success": False,

                "message": "No image selected."

            }), 400

        if not allowed_file(uploaded_image.filename):

            return jsonify({

                "success": False,

                "message": "Unsupported image format."

            }), 400

        filename = secure_filename(
            uploaded_image.filename
        )

        image_path = os.path.join(

            app.config["UPLOAD_FOLDER"],

            filename

        )

        uploaded_image.save(image_path)

        prediction = predict_disease(
            image_path
        )

        return jsonify({

            "success": True,

            "result": prediction

        })

    except Exception as error:

        return jsonify({

            "success": False,

            "error": str(error)

        }), 500
    # ==========================================================
# SERVER INFORMATION
# ==========================================================

def print_server_information():

    print("\n" + "=" * 60)
    print("AGRISENSE API SERVER")
    print("=" * 60)

    print("Host               : 127.0.0.1")
    print("Port               : 5000")
    print("Home Endpoint      : http://127.0.0.1:5000/")
    print("Health Endpoint    : http://127.0.0.1:5000/health")
    print("Prediction Endpoint: http://127.0.0.1:5000/predict")

    print("=" * 60)

    if MODEL is None:

        print("Prediction Mode    : Demo Mode")

    else:

        print("Prediction Mode    : Trained Model")

    print("Upload Folder      :", UPLOAD_FOLDER)
    print("Supported Formats  : JPG, JPEG, PNG")

    print("=" * 60)


# ==========================================================
# APPLICATION ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    print_server_information()

    print("\nStarting Flask Server...")
    print("-" * 60)

    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )