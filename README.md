# Text-Generate-Gemini-AI---Python

AI-powered text generation using Gemini. Python implementation for creative content creation.

## Requirements

- Python 3.8+
- Install required dependencies using:

```bash
pip install -r requirements.txt
```
## env

API_KEY=your-key-here
MODEL=gemini-pro 

To start the FastAPI application, run:
```bash
uvicorn app:app --reload
```

## TEST
```bash
{
  "request_type": "Description",
  "character_limit": 200,
  "sample_note": "AI-powered text generation"
}
```

## Example:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/generate' \
  -H 'Content-Type: application/json' \
  -d '{
  "request_type": "Description",
  "character_limit": 200,
  "sample_note": "AI-powered text generation"
}'
```
## Response:
```bash
{
  "detailed_description": "AI-powered text generation is transforming the way creative content is produced, enabling faster, more efficient workflows."
}
```

### Explanation of Sections:
- **Requirements**: Lists the dependencies and installation instructions.
- **Setup**: Describes how to set up the project, including creating the `.env` file for your API key.
- **Running the Server**: Explains how to start the FastAPI server.
- **Endpoints**: Describes the `POST /generate` API and how to use it with an example.
- **Security**: Reminds to keep sensitive keys private by adding `.env` to `.gitignore`.
