import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import DATABASES
from databases.arangodb import ArangoDB
from loaders.load_dataset import load_profiles, load_relationships

db = ArangoDB(
    DATABASES["ArangoDB"]["uri"],
    DATABASES["ArangoDB"]["user"],
    DATABASES["ArangoDB"]["password"],
)

db.connect()

print("Connected to ArangoDB")

# Create collections if they don't exist
if not db.db.has_collection("User"):
    db.db.create_collection("User")

if not db.db.has_collection("Friend"):
    db.db.create_collection("Friend", edge=True)

# Import Users
profiles = load_profiles(limit=1000)

print(f"Importing {len(profiles)} users...")

users = db.db.collection("User")

for profile in profiles:
    users.insert(
        {
            "_key": str(profile["id"]),
            "id": profile["id"]
        },
        overwrite=True
    )

print("Users imported successfully!")

# Import Relationships
relationships = load_relationships(limit=500)

print(f"Importing {len(relationships)} relationships...")

friends = db.db.collection("Friend")

for source, target in relationships:
    friends.insert(
        {
            "_from": f"User/{source}",
            "_to": f"User/{target}"
        },
        overwrite=True
    )

print("Relationships imported successfully!")

db.close()