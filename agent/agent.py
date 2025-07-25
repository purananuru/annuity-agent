
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from agent.tools import validate_dob, check_advisor_id, calculate_age, extract_demographics

llm = ChatOpenAI(temperature=0)

tools = [validate_dob, check_advisor_id, calculate_age, extract_demographics]

agent_executor = initialize_agent(
    tools, llm, agent=AgentType.CHAT_REACT_DESCRIPTION, verbose=True
)

def run_agent_on_inputs(dob: str, advisor_id: str, pdf_text: str):
    query = f"""
    Validate DOB {dob}, check if advisor ID {advisor_id} is valid.
    Then extract the state, sex, and medical conditions from the PDF text: {pdf_text[:500]}...
    Also, calculate the person's age.
    """
    return agent_executor.run(query)
