import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.llm_pick import pick_llm

llm_object = pick_llm("high")  # Example usage: pick the LLM based on the desired level
print(llm_object.invoke("What is the capital of France?"))  # Example invocation of the selected LLM