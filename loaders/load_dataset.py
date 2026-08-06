import csv
import os

# Get absolute path to the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")

# Sample dataset files
PROFILES_FILE = os.path.join(DATASET_DIR, "sample_profiles.txt")
RELATIONSHIPS_FILE = os.path.join(DATASET_DIR, "sample_relationships.txt")


def load_profiles(limit=None):
    """
    Load user profiles from the dataset.
    Returns a list of dictionaries.
    """
    profiles = []

    with open(PROFILES_FILE, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")

        for i, row in enumerate(reader):
            if limit is not None and i >= limit:
                break

            if len(row) == 0:
                continue

            profiles.append({
                "id": row[0],
                "data": row
            })

    return profiles


def load_relationships(limit=None):
    """
    Load relationships from the dataset.
    Returns a list of tuples.
    """
    relationships = []

    with open(RELATIONSHIPS_FILE, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")

        for i, row in enumerate(reader):
            if limit is not None and i >= limit:
                break

            if len(row) < 2:
                continue

            relationships.append((row[0], row[1]))

    return relationships


if __name__ == "__main__":
    print("Loading dataset...")

    profiles = load_profiles(limit=1000)
    relationships = load_relationships(limit=100000)

    print(f"Profiles loaded: {len(profiles)}")
    print(f"Relationships loaded: {len(relationships)}")