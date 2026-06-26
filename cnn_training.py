import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout
)

# Dataset Configuration
DATASET_PATH = "datasets/PlantVillage"
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
NUM_CLASSES = 15

print("=" * 50)
print("CNN Training Module")
print("=" * 50)

print(f"Dataset Path : {DATASET_PATH}")
print(f"Image Size   : {IMAGE_SIZE}")
print(f"Batch Size   : {BATCH_SIZE}")

# Check Dataset Availability
if os.path.exists(DATASET_PATH):
    print("Dataset Found")
else:
    print("Dataset Not Found")

# Create CNN Model
model = Sequential([
    Conv2D(
        32,
        (3, 3),
        activation="relu",
        input_shape=(224, 224, 3)
    ),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(
        64,
        (3, 3),
        activation="relu"
    ),
    MaxPooling2D(pool_size=(2, 2)),

    Flatten(),

    Dense(
        128,
        activation="relu"
    ),

    Dropout(0.5),

    Dense(
        NUM_CLASSES,
        activation="softmax"
    )
])

print("\nCNN Model Created Successfully\n")

model.summary()