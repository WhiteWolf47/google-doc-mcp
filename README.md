# Google Docs MCP

This project is a Multi-Channel Platform (MCP) server that automates the creation and editing of Google Docs using the Google Docs API.

## Prerequisites

- Python 3.7 or higher
- A Google Cloud project with the Google Docs API enabled
- A service account with a JSON key file

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/google-doc-mcp.git
   cd google-doc-mcp
   ```

2. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the environment variables**:

   - Create a `.env` file in the project root directory.
   - Add the path to your service account JSON file:

     ```plaintext
     SERVICE_ACCOUNT_FILE=path/to/your/service-account-file.json
     ```

## Running the MCP Server

To run the MCP server, use the following command:

```bash
uv run main_mcp.py
```

## Usage

- The server provides tools to create and update Google Docs.
- Use the `create_document` tool to create a new document.
- Use the `update_document` tool to update an existing document.

## License

This project is licensed under the MIT License.