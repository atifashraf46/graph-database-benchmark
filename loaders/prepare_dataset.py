import os

DATASET_DIR = "dataset"

RELATIONSHIP_FILE = os.path.join(
    DATASET_DIR,
    "soc-pokec-relationships.txt"
)

PROFILE_FILE = os.path.join(
    DATASET_DIR,
    "soc-pokec-profiles.txt"
)

OUTPUT_REL = os.path.join(
    DATASET_DIR,
    "sample_relationships.txt"
)

OUTPUT_PROFILE = os.path.join(
    DATASET_DIR,
    "sample_profiles.txt"
)

MAX_RELATIONSHIPS = 100000
MAX_PROFILES = 50000


def create_sample():

    print("Creating sample dataset...")

    # Sample relationships
    with open(RELATIONSHIP_FILE, "r", encoding="utf-8") as infile, \
         open(OUTPUT_REL, "w", encoding="utf-8") as outfile:

        for i, line in enumerate(infile):

            if i >= MAX_RELATIONSHIPS:
                break

            outfile.write(line)

    print("Relationships complete")

    # Sample profiles
    with open(PROFILE_FILE, "r", encoding="utf-8", errors="ignore") as infile, \
         open(OUTPUT_PROFILE, "w", encoding="utf-8") as outfile:

        for i, line in enumerate(infile):

            if i >= MAX_PROFILES:
                break

            outfile.write(line)

    print("Profiles complete")
    print("Dataset ready!")


if __name__ == "__main__":
    create_sample()