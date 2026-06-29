# Testing

## Test Case 1: Application Launch

**Input:** Run the application using:

```bash
streamlit run app.py
```

**Expected Result:**
The Streamlit application opens successfully in the browser.

**Status:** Passed

---

## Test Case 2: AI Response Generation

**Input:**
I'm confused about recursion.

**Expected Result:**
The application generates an AI response explaining the emotion and providing study tips.

**Status:** Passed

---

## Test Case 3: Empty Input

**Input:**
Leave the text area empty and click **Analyze**.

**Expected Result:**
The application displays:

```
Please enter your study problem.
```

**Status:** Passed

---

## Test Case 4: CSV Logging

**Input:**
Enter a study problem and click **Analyze**.

**Expected Result:**
A new row is added to `logs/interactions.csv` containing:
- Timestamp
- Student_Input
- AI_Response

**Status:** Passed