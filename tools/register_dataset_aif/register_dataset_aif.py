import os
from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


load_dotenv()

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["AI_FOUNDRY_CONNECTION_STRING"]
)

file_path = os.environ["JSONL_FILE_PATH"]

try:
    if os.path.exists(file_path):
        print(f"File found: {file_path}")
        print(f"File size: {os.path.getsize(file_path)} bytes")
        data_id, _ = project_client.upload_file(file_path)
        print(f"Data ID: {data_id}")
except Exception as e:
    print(f"Error uploading file: {e}")
