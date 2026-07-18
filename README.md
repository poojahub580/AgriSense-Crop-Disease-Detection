# 🌱 AgriSense Crop Disease Detection

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Flask](https://img.shields.io/badge/Flask-Web%20API-black)
![Deep Learning](https://img.shields.io/badge/MobileNetV2-Transfer%20Learning-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

# 📖 Overview

AgriSense is an AI-powered crop disease detection system developed using **TensorFlow**, **MobileNetV2 Transfer Learning**, and **Flask**. The application detects diseases from crop leaf images and provides prediction results with confidence scores, disease information, symptoms, recommendations, prevention tips, and prediction status through a responsive web interface.

The model is trained on the **PlantVillage Dataset** and supports disease classification for **Tomato**, **Potato**, and **Bell Pepper** crops.

---

# ✨ Features

- AI-powered Crop Disease Detection
- MobileNetV2 Transfer Learning
- PlantVillage Dataset Support
- Image Upload & Prediction
- Confidence Score Display
- Disease Description
- Symptoms Information
- Treatment Recommendations
- Prevention Guidelines
- Prediction Status
- Responsive Web Interface
- Flask REST API
- Health Check API
- Postman API Testing
- Automatic EDA Report Generation
- Automatic Model Evaluation Reports

---

# 📂 Dataset

## Dataset

PlantVillage Dataset

## Supported Classes (15)

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

# 📈 Exploratory Data Analysis

EDA was performed before model training to understand the dataset.

Generated reports include:

- Class Distribution
- Class Distribution Pie Chart
- Sample Images
- Image Dimension Analysis
- Image Dimension Box Plot
- Dataset Statistics

All generated graphs are automatically saved inside the **reports/** folder.

---

# 📊 Model Performance

- Framework: TensorFlow / Keras
- Model: MobileNetV2 Transfer Learning
- Dataset: PlantVillage
- Classes: 15
- Input Size: 224 × 224
- Validation Accuracy: **91.79%**
- Prediction Time: Less than 2 seconds

Generated Evaluation Reports:

- Confusion Matrix
- Classification Report
- Precision
- Recall
- F1-Score
- Model Metrics

---

# 🛠 Technologies Used

## Programming

- Python

## Deep Learning

- TensorFlow
- Keras
- MobileNetV2

## Backend

- Flask

## Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2

## Libraries

- NumPy
- Pillow
- OpenCV
- Scikit-learn
- Matplotlib

## Tools

- VS Code
- Git
- GitHub
- Postman
- Jupyter Notebook

---

# 📁 Project Structure

```text
AgriSense-Crop-Disease-Detection/
│
├── artifacts/
│   └── crop_disease_model.keras
│
├── datasets/
│   └── PlantVillage/
│
├── notebooks/
│   ├── eda.ipynb
│   └── model_evaluation.ipynb
│
├── reports/
│   ├── class_distribution.png
│   ├── class_distribution_pie.png
│   ├── image_dimension_boxplot.png
│   ├── sample_images.png
│   ├── confusion_matrix.png
│   ├── classification_report.txt
│   └── model_metrics.txt
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
├── api_service.py
├── cnn_training.py
├── transfer_learning.py
├── image_preprocessing.py
├── disease_prediction.py
├── dataset_statistics.py
├── model_performance.py
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

Clone the repository

```bash
git clone https://github.com/poojahub580/AgriSense-Crop-Disease-Detection
```

Move into the project

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

Open your browser

```
http://127.0.0.1:5000
```

---

# 📷 Screenshots

Add screenshots inside the **screenshots/** folder and update this section if available.

---

# ✅ Project Status

- ✔ Dataset Preprocessing Completed
- ✔ Exploratory Data Analysis Completed
- ✔ Dataset Statistics Generated
- ✔ CNN Model Developed
- ✔ MobileNetV2 Transfer Learning Implemented
- ✔ Model Evaluation Completed
- ✔ Confusion Matrix Generated
- ✔ Classification Report Generated
- ✔ Precision, Recall & F1-Score Generated
- ✔ Automatic Report Generation
- ✔ Flask REST API Developed
- ✔ Health Endpoint Tested
- ✔ Prediction Endpoint Tested
- ✔ Postman API Testing Completed
- ✔ End-to-End Disease Prediction Verified
- ✔ Responsive Web Interface Completed
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
- More Crop Categories
- Improved Model Accuracy

---

# 👨‍💻 Developer

**Pooja Gupta**

AgriSense – Crop Disease Detection using TensorFlow, Flask, and MobileNetV2 Transfer Learning.

---

# 📄 License

This project was developed for educational and internship purposes.