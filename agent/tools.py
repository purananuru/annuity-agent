
from langchain.tools import tool
import re
import json
from datetime import datetime

ADVISOR_DB = json.load(open("db/advisor_db.json"))

@tool
def validate_dob(dob: str) -> str:
    match = re.match(r"\d{4}-\d{2}-\d{2}", dob)
    return "Valid" if match else "Invalid date format"

@tool
def check_advisor_id(advisor_id: str) -> str:
    return "Valid" if advisor_id in ADVISOR_DB else "Invalid advisor ID"

@tool
def calculate_age(dob: str) -> int:
    birth = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()
    return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

@tool
def extract_demographics(text: str) -> dict:
    result = {}
    state_match = re.search(r"State[:\s]+([A-Z]{2})", text)
    sex_match = re.search(r"Sex[:\s]+(Male|Female|Other)", text, re.I)
    conditions = ["diabetes", "hypertension", "asthma"]
    found = [c for c in conditions if c.lower() in text.lower()]

    result["state"] = state_match.group(1) if state_match else "Unknown"
    result["sex"] = sex_match.group(1).capitalize() if sex_match else "Unknown"
    result["medical_conditions"] = found
    return result
