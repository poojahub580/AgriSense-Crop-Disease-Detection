# 🌱 AgriSense Crop Disease Detection

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Flask](https://img.shields.io/badge/Flask-Web%20API-black)
![License](https://img.shields.io/badge/Project-Final%20Year-green)

---

# 📖 Overview

AgriSense is an AI-powered crop disease detection system developed using **TensorFlow**, **MobileNetV2 Transfer Learning**, and **Flask**. The application detects diseases from crop leaf images and provides detailed prediction results, confidence scores, disease information, symptoms, recommendations, prevention tips, and prediction status through a modern web interface.

The model is trained using the **PlantVillage Dataset** and supports disease classification for Tomato, Potato, and Bell Pepper crops.

---

# ✨ Features

- AI-powered Crop Disease Detection
- MobileNetV2 Transfer Learning Model
- PlantVillage Dataset Support
- Image Upload & Prediction
- Prediction Summary Dashboard
- Confidence Score with Progress Bar
- Disease Description
- Symptoms Information
- Treatment Recommendations
- Prevention Guidelines
- Prediction Timestamp
- Prediction Status
- Modern Responsive Web UI
- Flask REST API
- Health Check API
- Postman API Testing
- Image Preprocessing & Normalization

---

# 📂 Dataset

**Dataset Used**

PlantVillage Dataset

**Supported Crop Disease Classes (15)**

- Pepper__bell___Bacterial_spot
- Pepper__bell___healthy
- Potato___Early_blight
- Potato___Late_blight
- Potato___healthy
- Tomato_Bacterial_spot
- Tomato_Early_blight
- Tomato_Late_blight
- Tomato_Leaf_Mold
- Tomato_Septoria_leaf_spot
- Tomato_Spider_mites_Two_spotted_spider_mite
- Tomato__Target_Spot
- Tomato__Tomato_YellowLeaf__Curl_Virus
- Tomato__Tomato_mosaic_virus
- Tomato_healthy

---

# 📊 Model Performance

- Deep Learning Framework: TensorFlow/Keras
- Model Architecture: MobileNetV2 Transfer Learning
- Dataset: PlantVillage
- Supported Classes: 15
- Input Image Size: 224 × 224
- Prediction Time: Less than 2 seconds
- Prediction Output: Disease Name, Confidence Score, Symptoms, Prevention and Recommendation

---

# 🛠 Technologies Used

### Programming

- Python

### Deep Learning

- TensorFlow
- Keras

### Backend

- Flask

### Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

### Libraries

- NumPy
- OpenCV
- Pillow
- Scikit-learn

### API Testing

- Postman

---

# 📁 Project Structure

```
AgriSense-Crop-Disease-Detection/
│
├── artifacts/
│   └── crop_disease_model.keras
│
├── datasets/
│   └── PlantVillage/
│
├── reports/
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── uploads/
│
├── notebooks/
│   └── eda.ipynb
│
├── api_service.py
├── cnn_training.py
├── disease_prediction.py
├── image_preprocessing.py
├── model_evaluation.py
├── transfer_learning.py
├── requirements.txt
└── README.md
```

---

# 🌐 API Endpoints

## Home

```
GET /
```

Returns the Home Page.

---

## Health Check

```
GET /health
```

Returns API status and model health.

---

## Disease Prediction

```
POST /predict
```

Upload a crop leaf image using **form-data**.

Key

```
image
```

Supported Formats

- JPG
- JPEG
- PNG

Example Response

```json
{
  "success": true,
  "result": {
    "prediction": "Tomato_Early_blight",
    "confidence": 96.62,
    "status": "Prediction Completed"
  }
}
```

---

# ⚙ Installation

Clone Repository

```bash
git clone https://github.com/Aditya-1809/AgriSense-Crop-Disease-Detection.git
```

Move into project folder

```bash
cd AgriSense-Crop-Disease-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python api_service.py
```

Open in browser

```
http://127.0.0.1:5000
```

---

# 📷 Screenshots

### Home Page
![Home Page](screenshots/home_page.png)

### Features
![Features](screenshots/features.png)

### Prediction Summary
![Prediction Summary](screenshots/prediction_summary.png)

### Prediction Result
![Prediction Result](screenshots/prediction_result.png)

### Confidence Progress Bar
![Confidence Bar](screenshots/confidence_bar.png)

### Prediction Actions
![Prediction Actions](screenshots/prediction_actions.png)

### API Running
![API Running](screenshots/api_running.png)

---

# ✅ Project Status

- ✔ Dataset Preprocessing Completed
- ✔ Exploratory Data Analysis Completed
- ✔ CNN Model Developed
- ✔ MobileNetV2 Transfer Learning Implemented
- ✔ Model Evaluation Completed
- ✔ Flask REST API Developed
- ✔ Image Upload System Implemented
- ✔ Prediction Summary Dashboard Completed
- ✔ Confidence Progress Bar Added
- ✔ Disease Description, Symptoms & Prevention Added
- ✔ Health Endpoint Tested
- ✔ Prediction Endpoint Tested
- ✔ Postman API Testing Completed
- ✔ End-to-End Disease Prediction Verified
- ✔ Modern Responsive User Interface Completed
- ✔ Ready for Final Demonstration

---

# 🚀 Future Improvements

- Real-time Camera Detection
- Mobile Application
- Cloud Deployment
- User Authentication
- Prediction History
- PDF Report Generation
- Multi-language Support
- Additional Crop Support
- Improved Model Accuracy

---

# 👨‍💻 Developer

**Pooja Gupta**

AgriSense Crop Disease Detection

Developed using **TensorFlow**, **Flask**, and **MobileNetV2 Transfer Learning**.