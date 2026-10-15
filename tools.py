from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from tavily import TavilyClient
from typing import Dict,Any

load_dotenv()
tavily_client=TavilyClient()

@tool
def web_search(query : str) ->Dict[str, Any]:
    """tool for searching the web for information"""
    print(f"we are doing some research on {query}")
    return tavily_client.search(query)


# def print_document(name:str)->str:
#     """use this tool to generate the propre documetn for you student"""
#     return f"this is the document of {name}"


agent=create_agent(model="groq:openai/gpt-oss-120b",
                   tools=[web_search],
                #    system_prompt="you are an employee that use your tools for genrating documents.do not say anything else.for now make a default profile"
                )

response=agent.invoke(
    {"messages":[HumanMessage(content="Give me the latest news on indian cricket, word limit upto 40 words")]}    
)

print("*"*5+"this is the ai last response."+"*"*5)
print(response["messages"][-1].content)

# print("*"*5+"this is details messages"+"*"*5)
# print(response["messages"])


# print(print_document.invoke({"name":"kitty"}))




