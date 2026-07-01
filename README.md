AgriSense Crop Disease Detection
Overview
AgriSense is a deep learning-based crop disease detection system that identifies diseases from crop leaf images. The project uses the PlantVillage dataset and a Convolutional Neural Network (CNN) with TensorFlow/Keras to classify crop diseases. A Flask REST API is provided to perform disease prediction from uploaded images.

Features
Crop disease detection using Deep Learning
PlantVillage dataset support
Image preprocessing and normalization
CNN model training
Disease prediction from leaf images
Model evaluation
Flask REST API
Health Check API
Postman API testing
Confidence score for predictions
Dataset
Dataset Used:

PlantVillage Dataset
Supported Classes: 15

Pepper__bell___Bacterial_spot
Pepper__bell___healthy
Potato___Early_blight
Potato___Late_blight
Potato___healthy
Tomato_Bacterial_spot
Tomato_Early_blight
Tomato_Late_blight
Tomato_Leaf_Mold
Tomato_Septoria_leaf_spot
Tomato_Spider_mites_Two_spotted_spider_mite
Tomato__Target_Spot
Tomato__Tomato_YellowLeaf__Curl_Virus
Tomato__Tomato_mosaic_virus
Tomato_healthy
Technologies Used
Python
TensorFlow
Keras
Flask
NumPy
OpenCV
Pillow
Scikit-learn
Postman
Project Structure
AgriSense-Crop-Disease-Detection/
│
├── artifacts/
│   └── crop_disease_model.keras
│
├── datasets/
│   └── PlantVillage/
│
├── uploads/
│
├── cnn_training.py
├── image_preprocessing.py
├── disease_prediction.py
├── model_evaluation.py
├── api_service.py
├── transfer_learning.py
├── requirements.txt
└── README.md
API Endpoints
Home
GET /

Returns project information.

Health Check
GET /health

Returns server and model status.

Disease Prediction
POST /predict

Upload a crop leaf image using form-data.

Key:

image
Supported Formats:

JPG
JPEG
PNG
Example Response

{
    "success": true,
    "result": {
        "prediction": "Pepper__bell___Bacterial_spot",
        "confidence": 96.62,
        "status": "Prediction Completed"
    }
}
Installation
pip install -r requirements.txt
Run the API

python api_service.py
Project Status
Dataset preprocessing completed
CNN model implemented
Transfer Learning implemented
Model evaluation completed
Flask API completed
Health endpoint tested
Prediction endpoint tested
Postman API testing completed
End-to-end disease prediction verified
Future Improvements
Web Dashboard
Mobile Application
Real-time Camera Detection
Cloud Deployment
Higher Model Accuracy
Support for Additional Crop Diseases
Developer
Pooja Gupta

AgriSense Crop Disease Detection Project