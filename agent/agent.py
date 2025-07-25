
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from agent.tools import validate_dob, check_advisor_id

llm = ChatOpenAI(temperature=0)

tools = [validate_dob, check_advisor_id]

agent_executor = initialize_agent(
    tools, llm, agent=AgentType.CHAT_REACT_DESCRIPTION, verbose=True
)

def run_agent_on_inputs(dob: str, advisor_id: str):
    return agent_executor.run(f"Validate DOB {dob} and advisor ID {advisor_id}")
