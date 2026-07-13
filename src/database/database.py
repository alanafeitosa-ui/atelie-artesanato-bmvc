import os 
from connection import get_connection

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(BASE_DIR, "schema.sql")

def initializate_database():
    connection = get_connection()
    try:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as file: schema = file.read()
        connection.executescript(schema)
        connection.commit()
        print("Database initialized sucessfuly")
    except Exception as error:
        connection.rollback()
        print(f"Database initialization faildes: {error}")
        raise
    finally:
        connection.close()

if __name__ == "__main__":
    initializate_database()