import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras import Input
from tensorflow.keras.layers import (
    GlobalAveragePooling2D,
    Dense,
    Dropout
)
from tensorflow.keras.applications import MobileNetV2


print("=" * 60)
print("AGRISENSE - TRANSFER LEARNING MODULE")
print("=" * 60)

DATASET_PATH = "datasets/PlantVillage"

IMAGE_HEIGHT = 224
IMAGE_WIDTH = 224

NUMBER_OF_CLASSES = 15

LEARNING_RATE = 0.0001

print("\nPROJECT CONFIGURATION")
print("-" * 60)
print(f"Dataset Path      : {DATASET_PATH}")
print(f"Image Size        : {IMAGE_HEIGHT} x {IMAGE_WIDTH}")
print(f"Total Classes     : {NUMBER_OF_CLASSES}")
print(f"Learning Rate     : {LEARNING_RATE}")
print("\nLOADING PRE-TRAINED MODEL")
print("-" * 60)

base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3)
)

print("[SUCCESS] MobileNetV2 Loaded Successfully")

print("\nFREEZING BASE MODEL")
print("-" * 60)

base_model.trainable = False

print("[SUCCESS] Pre-trained Layers Frozen")
print("\nBUILDING TRANSFER LEARNING MODEL")
print("-" * 60)

transfer_learning_model = Sequential([
    Input(shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3)),
    base_model,
    GlobalAveragePooling2D(),
    Dense(
        256,
        activation="relu"
    ),
    Dropout(0.5),
    Dense(
        128,
        activation="relu"
    ),
    Dropout(0.3),
    Dense(
        NUMBER_OF_CLASSES,
        activation="softmax"
    )
])

print("[SUCCESS] Transfer Learning Model Created")
print("\nCOMPILING MODEL")
print("-" * 60)

transfer_learning_model.compile(
    optimizer=tf.keras.optimizers.Adam(
        learning_rate=LEARNING_RATE
    ),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("[SUCCESS] Model Compiled Successfully")
print("\nMODEL SUMMARY")
print("-" * 60)

transfer_learning_model.summary()

print("\nTransfer Learning Module Ready")