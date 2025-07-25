
from langsmith_setup import init_tracing
from agent.extractor import extract_text_from_pdf
from agent.agent import run_agent_on_inputs

init_tracing()

pdf_text = extract_text_from_pdf("data/sample.pdf")

# Mocked values for demo
dob = "1990-02-14"
advisor_id = "A123"

result = run_agent_on_inputs(dob, advisor_id, pdf_text)

print("Validation & Demographics Result:\n", result)
