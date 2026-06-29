# Deployment

## Local Deployment

### Prerequisites
- Python 3.9 or above
- Virtual Environment (venv)
- Google Gemini API Key
- Streamlit

### Steps

1. Open the project folder.
2. Activate the virtual environment.

```bash
source venv/bin/activate
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Add the Gemini API key to the `.env` file.

```text
GEMINI_API_KEY=YOUR_API_KEY
```

5. Run the application.

```bash
streamlit run app.py
```

6. Open the browser at:

```
http://localhost:8501
```

The AI Learning Assistant is now ready to use.
