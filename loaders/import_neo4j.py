from config import DATABASES
from databases.neo4j import Neo4jDB
from loaders.load_dataset import load_profiles, load_relationships

db = Neo4jDB(
    DATABASES["Neo4j"]["uri"],
    DATABASES["Neo4j"]["user"],
    DATABASES["Neo4j"]["password"],
)

db.connect()

print("Connected to Neo4j")

# Import Users
profiles = load_profiles(limit=1000)

print(f"Importing {len(profiles)} users...")

for profile in profiles:
    db.execute_write(
        """
        MERGE (u:User {id:$id})
        """,
        {
            "id": profile["id"]
        }
    )

print("Users imported successfully!")

# Import Relationships
relationships = load_relationships(limit=500)

print(f"Importing {len(relationships)} relationships...")

for source, target in relationships:
    db.execute_write(
        """
        MATCH (a:User {id:$source})
        MATCH (b:User {id:$target})
        MERGE (a)-[:FRIEND]->(b)
        """,
        {
            "source": source,
            "target": target
        }
    )

print("Relationships imported successfully!")

db.close()