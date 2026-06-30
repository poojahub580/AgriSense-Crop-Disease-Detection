import os
import tensorflow as tf

from tensorflow.keras import Sequential
from tensorflow.keras import Input

from tensorflow.keras.layers import (
    GlobalAveragePooling2D,
    Dense,
    Dropout
)

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint
)

print("=" * 60)
print("AGRISENSE - TRANSFER LEARNING TRAINING")
print("=" * 60)

# ======================================================
# PROJECT CONFIGURATION
# ======================================================

DATASET_PATH = "datasets/PlantVillage"

MODEL_DIRECTORY = "artifacts"

MODEL_NAME = "crop_disease_model.keras"

IMAGE_HEIGHT = 224
IMAGE_WIDTH = 224

BATCH_SIZE = 32

EPOCHS = 10

LEARNING_RATE = 0.0001

if not os.path.exists(MODEL_DIRECTORY):
    os.makedirs(MODEL_DIRECTORY)

print("\nPROJECT CONFIGURATION")
print("-" * 60)

print("Dataset Path :", DATASET_PATH)
print("Image Size   :", (IMAGE_HEIGHT, IMAGE_WIDTH))
print("Batch Size   :", BATCH_SIZE)
print("Epochs       :", EPOCHS)
print("Learning Rate:", LEARNING_RATE)

# ======================================================
# DATASET LOADING
# ======================================================

print("\nLOADING DATASET")
print("-" * 60)

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.20,
    subset="training",
    seed=123,
    image_size=(IMAGE_HEIGHT, IMAGE_WIDTH),
    batch_size=BATCH_SIZE,
    label_mode="categorical"
)

validation_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.20,
    subset="validation",
    seed=123,
    image_size=(IMAGE_HEIGHT, IMAGE_WIDTH),
    batch_size=BATCH_SIZE,
    label_mode="categorical"
)

CLASS_NAMES = train_dataset.class_names

NUMBER_OF_CLASSES = len(CLASS_NAMES)

print("[SUCCESS] Dataset Loaded")

print("\nCLASS INFORMATION")
print("-" * 60)

for index, class_name in enumerate(CLASS_NAMES):
    print(f"{index + 1}. {class_name}")

print("-" * 60)

print("Total Classes :", NUMBER_OF_CLASSES)
# ======================================================
# DATASET PREPROCESSING
# ======================================================

print("\nPREPROCESSING DATASET")
print("-" * 60)

AUTOTUNE = tf.data.AUTOTUNE

train_dataset = train_dataset.map(
    lambda x, y: (preprocess_input(x), y),
    num_parallel_calls=AUTOTUNE
)

validation_dataset = validation_dataset.map(
    lambda x, y: (preprocess_input(x), y),
    num_parallel_calls=AUTOTUNE
)

train_dataset = train_dataset.prefetch(
    buffer_size=AUTOTUNE
)

validation_dataset = validation_dataset.prefetch(
    buffer_size=AUTOTUNE
)

print("[SUCCESS] Dataset Optimized")


# ======================================================
# LOAD PRE-TRAINED MODEL
# ======================================================

print("\nLOADING PRE-TRAINED MODEL")
print("-" * 60)

base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3)
)

print("[SUCCESS] MobileNetV2 Loaded")


# ======================================================
# FREEZE BASE MODEL
# ======================================================

base_model.trainable = False

print("[SUCCESS] Pre-trained Layers Frozen")


# ======================================================
# BUILD TRANSFER LEARNING MODEL
# ======================================================

print("\nBUILDING MODEL")
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

print("[SUCCESS] Model Created")
# ======================================================
# COMPILE MODEL
# ======================================================

print("\nCOMPILING MODEL")
print("-" * 60)

transfer_learning_model.compile(

    optimizer=tf.keras.optimizers.Adam(
        learning_rate=LEARNING_RATE
    ),

    loss="categorical_crossentropy",

    metrics=[
        "accuracy"
    ]

)

print("[SUCCESS] Model Compiled")


# ======================================================
# MODEL SUMMARY
# ======================================================

print("\nMODEL SUMMARY")
print("-" * 60)

transfer_learning_model.summary()


# ======================================================
# TRAINING CALLBACKS
# ======================================================

print("\nCONFIGURING TRAINING")
print("-" * 60)

checkpoint = ModelCheckpoint(

    filepath=os.path.join(
        MODEL_DIRECTORY,
        MODEL_NAME
    ),

    monitor="val_accuracy",

    mode="max",

    save_best_only=True,

    verbose=1

)

early_stopping = EarlyStopping(

    monitor="val_loss",

    patience=3,

    restore_best_weights=True,

    verbose=1

)

print("[SUCCESS] Training Callbacks Ready")


# ======================================================
# START TRAINING
# ======================================================

print("\nSTARTING MODEL TRAINING")
print("-" * 60)

history = transfer_learning_model.fit(

    train_dataset,

    validation_data=validation_dataset,

    epochs=EPOCHS,

    callbacks=[
        checkpoint,
        early_stopping
    ]

)

print("\n[SUCCESS] Training Completed")