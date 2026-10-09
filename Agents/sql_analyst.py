import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.llm_pick import pick_llm
from Models.schema import AgentSchema


#----------------------------AI Agent Class-------------------------


def curate_ques(state: AgentSchema) -> AgentSchema:


    user_question = state.user_question
    llm = pick_llm("low")
    response = llm.invoke(f"Curate the following user question for SQL query generation: {user_question}")

    state.curated_ques = response
    return state

def prompt_query_context(state: AgentSchema) -> AgentSchema:
    curated_ques = state.curated_ques
    