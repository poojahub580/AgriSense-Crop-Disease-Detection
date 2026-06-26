import os

dataset_path = "datasets/PlantVillage"

print("=" * 50)
print("PlantVillage Dataset Analysis")
print("=" * 50)

if os.path.exists(dataset_path):

    classes = [
        folder for folder in os.listdir(dataset_path)
        if os.path.isdir(os.path.join(dataset_path, folder))
    ]

    print(f"Dataset Folder Found")
    print(f"Total Classes: {len(classes)}")

    total_images = 0

    for class_name in classes:
        class_path = os.path.join(dataset_path, class_name)

        image_count = len([
            file for file in os.listdir(class_path)
            if file.endswith((".jpg", ".jpeg", ".png"))
        ])

        total_images += image_count

        print(f"{class_name}: {image_count} images")

    print("-" * 50)
    print(f"Total Images: {total_images}")

else:
    print("Dataset Folder Not Found")