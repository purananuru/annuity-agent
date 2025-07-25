
from langchain.tools import tool
import re
import json

ADVISOR_DB = json.load(open("db/advisor_db.json"))

@tool
def validate_dob(dob: str) -> str:
    match = re.match(r"\d{4}-\d{2}-\d{2}", dob)
    return "Valid" if match else "Invalid date format"

@tool
def check_advisor_id(advisor_id: str) -> str:
    return "Valid" if advisor_id in ADVISOR_DB else "Invalid advisor ID"
