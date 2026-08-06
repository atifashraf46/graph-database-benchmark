from config import DATABASES
from databases.neo4j import Neo4jDB

db = Neo4jDB(
    DATABASES["Neo4j"]["uri"],
    DATABASES["Neo4j"]["user"],
    DATABASES["Neo4j"]["password"]
)

try:
    db.connect()
    print("✅ Connected Successfully")

    result = db.execute("RETURN 1 AS number")
    print(result)

    db.close()

except Exception as e:
    print("❌ Error:")
    print(type(e).__name__)
    print(e)