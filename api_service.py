import json
import os
from datetime import datetime

import numpy as np
import tensorflow as tf

from flask import (
    Flask,
    jsonify,
    request,
    render_template
)

from werkzeug.utils import secure_filename

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

from data.disease_info import DISEASE_INFO


# ==========================================================
# AGRISENSE AI
# ==========================================================

print("=" * 70)
print("🌱 AGRISENSE AI - CROP DISEASE DETECTION")
print("=" * 70)


# ==========================================================
# PROJECT CONFIGURATION
# ==========================================================

MODEL_PATH = "artifacts/crop_disease_model.keras"

UPLOAD_FOLDER = "static/images"

IMAGE_SIZE = (224, 224)

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

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

print("✅ Upload directory ready")


# ==========================================================
# FILE VALIDATION
# ==========================================================

def allowed_file(filename):

    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# ==========================================================
# MODEL LOADING
# ==========================================================

def load_prediction_model():

    if not os.path.exists(MODEL_PATH):

        print("⚠ Model not found")

        print("Running in Demo Mode")

        return None

    try:

        model = tf.keras.models.load_model(
            MODEL_PATH
        )

        print("✅ Model Loaded Successfully")

        return model

    except Exception as error:

        print("❌ Failed to load model")

        print(error)

        return None


MODEL = load_prediction_model()
# ==========================================================
# IMAGE PREPROCESSING
# ==========================================================

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

def predict_disease(image_path):

    processed_image = preprocess_image(image_path)

    # -------------------------------
    # DEMO MODE
    # -------------------------------

    if MODEL is None:

        disease = "Tomato_healthy"

        info = DISEASE_INFO.get(
            disease,
            {}
        )

        return {

            "status": "Demo Mode",

            "prediction": disease,

            "confidence": 100.0,

            "crop": info.get(
                "crop",
                "Tomato"
            ),

            "severity": info.get(
                "severity",
                "None"
            ),

            "description": info.get(
                "description",
                "No description available."
            ),

            "symptoms": info.get(
                "symptoms",
                []
            ),

            "recommendation": info.get(
                "recommendation",
                []
            ),

            "prevention": info.get(
                "prevention",
                []
            ),

            "prediction_time": datetime.now().strftime(
                "%d %B %Y %I:%M %p"
            )

        }

    # -------------------------------
    # MODEL PREDICTION
    # -------------------------------

    prediction = MODEL.predict(
        processed_image,
        verbose=0
    )

    predicted_index = int(
        np.argmax(prediction)
    )

    confidence = round(
        float(np.max(prediction)) * 100,
        2
    )

    disease = CLASS_NAMES[
        predicted_index
    ]

    info = DISEASE_INFO.get(
        disease,
        {
            "crop": "Unknown",
            "severity": "Unknown",
            "description": "Information not available.",
            "symptoms": [],
            "recommendation": [],
            "prevention": []
        }
    )

    return {

        "status": "Prediction Completed",

        "prediction": disease,

        "confidence": confidence,

        "crop": info["crop"],

        "severity": info["severity"],

        "description": info["description"],

        "symptoms": info["symptoms"],

        "recommendation": info["recommendation"],

        "prevention": info["prevention"],

        "prediction_time": datetime.now().strftime(
            "%d %B %Y %I:%M %p"
        )

    }
# ==========================================================
# HOME ROUTE
# ==========================================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================================
# HEALTH CHECK ROUTE
# ==========================================================

@app.route("/health")
def health():

    return jsonify({

        "server": "Online",

        "model_status":
            "Loaded" if MODEL is not None else "Demo Mode",

        "classes": len(CLASS_NAMES),

        "image_size": IMAGE_SIZE,

        "upload_folder": UPLOAD_FOLDER

    })


# ==========================================================
# DISEASE PREDICTION ROUTE
# ==========================================================

@app.route("/predict", methods=["POST"])
def prediction_api():

    try:

        # --------------------------------------
        # Validate uploaded file
        # --------------------------------------

        if "file" not in request.files:

            return render_template(

                "result.html",

                prediction="No image uploaded.",

                confidence="0%",

                status="Upload Failed"

            )

        uploaded_image = request.files["file"]

        if uploaded_image.filename == "":

            return render_template(

                "result.html",

                prediction="No image selected.",

                confidence="0%",

                status="Upload Failed"

            )

        if not allowed_file(uploaded_image.filename):

            return render_template(

                "result.html",

                prediction="Unsupported image format.",

                confidence="0%",

                status="Only JPG, JPEG and PNG images are supported."

            )

        # --------------------------------------
        # Save uploaded image
        # --------------------------------------

        filename = secure_filename(
            uploaded_image.filename
        )

        image_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        uploaded_image.save(image_path)

        # --------------------------------------
        # Predict disease
        # --------------------------------------

        result = predict_disease(image_path)

        # --------------------------------------
        # Send data to result page
        # --------------------------------------
        display_prediction = result["prediction"].replace("__", " - ").replace("_", " ")

        # Load existing prediction history
        history_file = "prediction_history.json"

        if os.path.exists(history_file):
           with open(history_file, "r") as file:
             history = json.load(file)
        else:
         history = []

        # Add current prediction
        history.insert(0, {
        "crop": result["crop"],
        "prediction": display_prediction,
        "confidence": f'{result["confidence"]}%',
        "time": result["prediction_time"]
        })

        # Keep only the latest 5 predictions
        history = history[:5]

        # Save updated history
        with open(history_file, "w") as file:
         json.dump(history, file, indent=4)

        return render_template(

            "result.html",

            image_file=filename,

            crop=result["crop"],

            prediction=display_prediction,

            confidence=f'{result["confidence"]}%',

            severity=result["severity"],

            description=result["description"],

            symptoms=result["symptoms"],

            recommendation=result["recommendation"],

            prevention=result["prevention"],

            prediction_time=result["prediction_time"],

            status=result["status"],

            history=history

         )

    except Exception as error:

        return render_template(

            "result.html",

            prediction="Prediction Failed",

            confidence="0%",

            status=str(error)

        )
    # ==========================================================
# SERVER INFORMATION
# ==========================================================

def print_server_information():

    print("\n" + "=" * 70)

    print("🌱 AGRISENSE AI SERVER")

    print("=" * 70)

    print(f"{'Host':25}: 127.0.0.1")
    print(f"{'Port':25}: 5000")
    print(f"{'Home Page':25}: http://127.0.0.1:5000/")
    print(f"{'Prediction Endpoint':25}: /predict")
    print(f"{'Health Endpoint':25}: /health")
    print(f"{'Upload Folder':25}: {UPLOAD_FOLDER}")
    print(f"{'Image Size':25}: {IMAGE_SIZE[0]} x {IMAGE_SIZE[1]}")
    print(f"{'Supported Formats':25}: JPG, JPEG, PNG")
    print(f"{'Total Classes':25}: {len(CLASS_NAMES)}")

    if MODEL is None:
        print(f"{'Prediction Mode':25}: Demo Mode")
    else:
        print(f"{'Prediction Mode':25}: Trained Model")

    print("=" * 70)


# ==========================================================
# APPLICATION ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    print_server_information()

    print("\n🚀 Starting AgriSense AI Server...")
    print("-" * 70)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )