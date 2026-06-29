# Environment Setup

## Hardware Requirements

- Processor: Intel i3 or above
- RAM: Minimum 4 GB (8 GB recommended)
- Storage: Minimum 2 GB free disk space
- Internet Connection: Required for package installation and Gemini API access

---

## Software Requirements

- Operating System: macOS / Windows / Linux
- Python 3.9 or above
- Visual Studio Code
- Streamlit
- Google Gemini API
- Virtual Environment (venv)

---

## Environment Setup Steps

### Step 1: Create Project Folder

Create a folder named:

```
AI-Learning-Assistant
```

---

### Step 2: Create a Virtual Environment

Run the following command:

```bash
python3 -m venv venv
```

---

### Step 3: Activate the Virtual Environment

For macOS/Linux:

```bash
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

---

### Step 4: Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

---

### Step 5: Configure Environment Variables

Create a `.env` file in the project root and add:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual Google Gemini API key.

---

### Step 6: Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

---

## Project Folder Structure

```text
AI-Learning-Assistant/
│── app.py
│── requirements.txt
│── README.md
│── .env
│
├── data/
├── docs/
├── images/
├── logs/
├── models/
├── utils/
└── venv/
```

---

## Verification

After completing the setup:

- Virtual environment is activated.
- All required packages are installed.
- Gemini API key is configured.
- Streamlit application launches successfully.
- AI responses are generated.
- User interactions are saved in `logs/interactions.csv`.

---

## Setup Status

**Environment Setup Completed Successfully**