#to switch between different LLMs, you can change the model name in the `llm_pick.py` file. For example, if you want to use GPT-4 instead of GPT-3, you can modify the model name in the code accordingly. Make sure to also update any relevant parameters or configurations that are specific to the chosen model.
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
def pick_llm(Level : str):
    """
    Function to pick the appropriate LLM based on the specified level.
    
    Args:
        Level (str): The level of the LLM to be used (e.g., 'basic', 'advanced', 'expert').
        
    Returns:
        str: The name of the selected LLM model.
    """
    if Level.lower() == 'low':
        llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", temperature=0, max_output_tokens=1024)
    elif Level.lower() == 'medium':
        llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0, max_output_tokens=2048)
    elif Level.lower() == 'high':
        llm = ChatGoogleGenerativeAI(model="gemini-3.1-pro-preview", temperature=0, max_output_tokens=4096)
    else:
        raise ValueError(f"unsupported Level: {Level}")
    return llm

llm_object = pick_llm("high")  # Example usage: pick the LLM based on the desired level
print(llm_object.invoke("What is the capital of France?"))  # Example invocation of the selected LLM