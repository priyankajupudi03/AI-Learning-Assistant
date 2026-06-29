# Project Workflow

## Step 1: User Input
The student enters a study-related problem into the Streamlit application.

## Step 2: Gemini API Processing
The input is sent to the Google Gemini API through the `get_response()` function.

## Step 3: AI Analysis
Gemini analyzes the student's problem, identifies the likely emotion, and generates personalized study guidance.

## Step 4: Display Response
The AI-generated response is displayed on the Streamlit interface.

## Step 5: Interaction Logging
The student's input, AI response, and timestamp are stored in `logs/interactions.csv` for future analysis.

## Workflow Diagram

User Input
      ↓
Streamlit Interface
      ↓
Gemini API
      ↓
AI Response Generation
      ↓
Display Response
      ↓
Save to CSV Log