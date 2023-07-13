# * Import Python Module
import os

#  Read key-value pairs from a .env file and set them as environment variables
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database_name = os.getenv("DATABASE_NAME")
host = os.getenv("DB_HOST")

# * Define the database host URI
host_uri = f"mongodb+srv://{user}:{password}@{host}/{database_name}"
