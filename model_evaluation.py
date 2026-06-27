import os
from collections import defaultdict

DATASET_PATH = "datasets/PlantVillage"


def print_header():
    print("=" * 60)
    print("AGRISENSE - MODEL EVALUATION MODULE")
    print("=" * 60)


def check_dataset_exists(path):
    if os.path.exists(path):
        print(f"[SUCCESS] Dataset Found: {path}")
        return True

    print(f"[ERROR] Dataset Not Found: {path}")
    return False


def get_class_directories(path):
    classes = []

    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            classes.append(item)

    return sorted(classes)


def count_images_in_class(class_path):
    image_count = 0

    for file in os.listdir(class_path):
        if file.lower().endswith(
            (".jpg", ".jpeg", ".png")
        ):
            image_count += 1

    return image_count


def generate_dataset_statistics(path):
    classes = get_class_directories(path)

    print("\nDATASET OVERVIEW")
    print("-" * 60)

    print(f"Total Classes : {len(classes)}")

    total_images = 0

    class_statistics = defaultdict(int)

    print("\nCLASS-WISE IMAGE COUNT")
    print("-" * 60)

    for class_name in classes:

        class_path = os.path.join(path, class_name)

        image_count = count_images_in_class(class_path)

        class_statistics[class_name] = image_count

        total_images += image_count

        print(
            f"{class_name:<40} {image_count:>6}"
        )

    print("-" * 60)

    print(f"TOTAL IMAGES : {total_images}")

    return class_statistics, total_images


def display_dataset_balance(class_statistics):

    print("\nDATASET BALANCE ANALYSIS")
    print("-" * 60)

    if not class_statistics:
        print("No statistics available.")
        return

    max_class = max(
        class_statistics,
        key=class_statistics.get
    )

    min_class = min(
        class_statistics,
        key=class_statistics.get
    )

    print(
        f"Largest Class : {max_class}"
    )

    print(
        f"Images        : {class_statistics[max_class]}"
    )

    print()

    print(
        f"Smallest Class: {min_class}"
    )

    print(
        f"Images        : {class_statistics[min_class]}"
    )


def main():

    print_header()

    if not check_dataset_exists(DATASET_PATH):
        return

    class_statistics, total_images = (
        generate_dataset_statistics(
            DATASET_PATH
        )
    )

    display_dataset_balance(
        class_statistics
    )

    print("\nEvaluation Completed Successfully")


if __name__ == "__main__":
    main()