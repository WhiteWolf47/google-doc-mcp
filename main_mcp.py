import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()

# Path to the service account key file
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

# Scopes for the Google Docs API
SCOPES = ['https://www.googleapis.com/auth/documents']

# Authenticate and build the service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
docs_service = build('docs', 'v1', credentials=credentials)

# Create an MCP server
mcp = FastMCP("GoogleDocsMCP")

@mcp.tool()
def create_document(title: str) -> str:
    """Create a new Google Doc and return its document ID."""
    document = docs_service.documents().create(body={
        'title': title
    }).execute()
    document_id = document.get('documentId')
    print(f'Document created with ID: {document_id}')
    return document_id

@mcp.tool()
def update_document(document_id: str, content: str):
    """Update a Google Doc with the given content."""
    requests = [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': content
            }
        }
    ]
    result = docs_service.documents().batchUpdate(
        documentId=document_id, body={'requests': requests}).execute()
    print(f'Document updated: {result}')

if __name__ == "__main__":
    mcp.run()


