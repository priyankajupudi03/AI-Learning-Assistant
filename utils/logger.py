import csv
import os
from datetime import datetime

LOG_FILE = "logs/interactions.csv"

def save_interaction(user_input, ai_response):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Timestamp", "Student_Input", "AI_Response"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            user_input,
            ai_response
        ])