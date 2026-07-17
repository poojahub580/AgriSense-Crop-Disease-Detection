import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay

from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# ======================================================
# CONFIGURATION
# ======================================================

DATASET_PATH = "datasets/PlantVillage"
MODEL_PATH = "artifacts/crop_disease_model.keras"
REPORTS_FOLDER = "reports"

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

os.makedirs(REPORTS_FOLDER, exist_ok=True)

print("=" * 60)
print("AGRISENSE - MODEL PERFORMANCE")
print("=" * 60)

# ======================================================
# LOAD MODEL
# ======================================================

print("\nLoading trained model...")

model = load_model(MODEL_PATH)

print("[SUCCESS] Model Loaded")

# ======================================================
# LOAD VALIDATION DATASET
# ======================================================

print("\nLoading validation dataset...")

validation_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.20,
    subset="validation",
    seed=123,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="categorical",
    shuffle=False
)

class_names = validation_dataset.class_names

validation_dataset = validation_dataset.map(
    lambda x, y: (preprocess_input(x), y)
)

# ======================================================
# EVALUATE MODEL
# ======================================================

print("\nEvaluating model...")

loss, accuracy = model.evaluate(validation_dataset)

print(f"\nValidation Loss     : {loss:.4f}")
print(f"Validation Accuracy : {accuracy*100:.2f}%")

# ======================================================
# PREDICTIONS
# ======================================================

print("\nGenerating predictions...")

y_true = []
y_pred = []

for images, labels in validation_dataset:

    predictions = model.predict(images, verbose=0)

    y_true.extend(np.argmax(labels.numpy(), axis=1))
    y_pred.extend(np.argmax(predictions, axis=1))

# ======================================================
# CLASSIFICATION REPORT
# ======================================================

print("\nClassification Report")
print("=" * 60)

report = classification_report(
    y_true,
    y_pred,
    labels=list(range(len(class_names))),
    target_names=class_names,
    zero_division=0
)

print(report)

report_path = os.path.join(REPORTS_FOLDER, "classification_report.txt")

with open(report_path, "w") as file:
    file.write(report)

print(f"\nReport saved to: {report_path}")

# ======================================================
# CONFUSION MATRIX
# ======================================================

cm = confusion_matrix(y_true, y_pred)

fig, ax = plt.subplots(figsize=(12, 12))

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=class_names
)

display.plot(
    cmap="Blues",
    xticks_rotation=90,
    ax=ax
)

plt.title("Confusion Matrix")

plt.tight_layout()

cm_path = os.path.join(
    REPORTS_FOLDER,
    "confusion_matrix.png"
)

plt.savefig(cm_path, dpi=300)

plt.close()

print(f"Confusion Matrix saved to: {cm_path}")

print("\n[SUCCESS] Model evaluation completed.")