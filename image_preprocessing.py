import os

dataset_path = "datasets/PlantVillage"

print("Dataset Path:", dataset_path)

if os.path.exists(dataset_path):
    print("Dataset folder found")
else:
    print("Dataset folder not found")