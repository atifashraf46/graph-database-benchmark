import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    "CognoDB": {
        "uri": os.getenv("COGNODB_URI"),
        "user": os.getenv("COGNODB_USER"),
        "password": os.getenv("COGNODB_PASSWORD"),
    },

    "Neo4j": {
        "uri": os.getenv("NEO4J_URI"),
        "user": os.getenv("NEO4J_USER"),
        "password": os.getenv("NEO4J_PASSWORD"),
    },

    "Memgraph": {
        "uri": os.getenv("MEMGRAPH_URI"),
        "user": os.getenv("MEMGRAPH_USER"),
        "password": os.getenv("MEMGRAPH_PASSWORD"),
    },

    "FalkorDB": {
        "host": os.getenv("FALKORDB_HOST"),
        "port": os.getenv("FALKORDB_PORT"),
        "user": os.getenv("FALKORDB_USER"),
        "password": os.getenv("FALKORDB_PASSWORD"),
    },

    "ArangoDB": {
        "uri": os.getenv("ARANGO_URI"),
        "user": os.getenv("ARANGO_USER"),
        "password": os.getenv("ARANGO_PASSWORD"),
    }
}

print("Neo4j URI:", DATABASES["Neo4j"]["uri"])
print("Neo4j User:", DATABASES["Neo4j"]["user"])

if DATABASES["Neo4j"]["password"]:
    print("Neo4j Password Length:", len(DATABASES["Neo4j"]["password"]))
else:
    print("Neo4j Password is EMPTY!")