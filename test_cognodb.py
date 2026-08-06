from config import DATABASES
from databases.cognodb import CognoDB

print("Testing CognoDB...")

db = CognoDB(
    DATABASES["CognoDB"]["uri"],
    DATABASES["CognoDB"]["user"],
    DATABASES["CognoDB"]["password"]
)

try:
    db.connect()
    print("✅ CognoDB Connected Successfully")
    db.close()
except Exception as e:
    print("❌ CognoDB Connection Failed")
    print(e)