import os
from collections import defaultdict

DATASET_PATH = "datasets/PlantVillage"


def print_header():
    print("=" * 60)
    print("AGRISENSE - IMAGE PREPROCESSING MODULE")
    print("=" * 60)


def validate_dataset_path(path):

    if os.path.exists(path):
        print(f"[SUCCESS] Dataset Found: {path}")
        return True

    print(f"[ERROR] Dataset Not Found: {path}")
    return False


def get_class_directories(path):

    classes = []

    for item in os.listdir(path):

        item_path = os.path.join(path, item)

        if (
            os.path.isdir(item_path)
            and item != "PlantVillage"
        ):
            classes.append(item)

    return sorted(classes)


def count_images(class_path):

    valid_extensions = (
        ".jpg",
        ".jpeg",
        ".png",
        ".JPG",
        ".JPEG",
        ".PNG"
    )

    image_count = 0

    for root, dirs, files in os.walk(class_path):

        for file in files:

            if file.endswith(valid_extensions):
                image_count += 1

    return image_count


def analyze_dataset(path):

    classes = get_class_directories(path)

    print("\nDATASET ANALYSIS")
    print("-" * 60)

    print(f"Total Classes : {len(classes)}")

    total_images = 0

    class_statistics = defaultdict(int)

    print("\nCLASS-WISE IMAGE COUNT")
    print("-" * 60)

    for class_name in classes:

        class_path = os.path.join(path, class_name)

        image_count = count_images(class_path)

        class_statistics[class_name] = image_count

        total_images += image_count

        print(
            f"{class_name:<45} {image_count:>6}"
        )

    print("-" * 60)

    print(f"TOTAL IMAGES : {total_images}")

    return class_statistics, total_images


def dataset_summary(class_statistics):

    print("\nDATASET SUMMARY")
    print("-" * 60)

    if not class_statistics:
        print("No dataset information available.")
        return

    largest_class = max(
        class_statistics,
        key=class_statistics.get
    )

    smallest_class = min(
        class_statistics,
        key=class_statistics.get
    )

    print(
        f"Largest Class  : {largest_class}"
    )

    print(
        f"Image Count    : {class_statistics[largest_class]}"
    )

    print()

    print(
        f"Smallest Class : {smallest_class}"
    )

    print(
        f"Image Count    : {class_statistics[smallest_class]}"
    )


def preprocessing_recommendations():

    print("\nPREPROCESSING RECOMMENDATIONS")
    print("-" * 60)

    print("1. Resize images to 224x224 pixels")
    print("2. Normalize pixel values between 0 and 1")
    print("3. Apply data augmentation")
    print("4. Remove corrupted images")
    print("5. Maintain class balance")
    print("6. Shuffle dataset before training")
    print("7. Split data into train, validation and test sets")


def main():

    print_header()

    if not validate_dataset_path(DATASET_PATH):
        return

    class_statistics, total_images = analyze_dataset(
        DATASET_PATH
    )

    dataset_summary(
        class_statistics
    )

    preprocessing_recommendations()

    print("\nImage Preprocessing Analysis Completed")


if __name__ == "__main__":
    main()