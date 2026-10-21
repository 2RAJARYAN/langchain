from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage,AIMessage

from tools import web_search
from photo_decoder import choose_image_file,build_image_message
from prompt import SYSTEM_CHEF_PROMPT,CHEF_PROMPT
import logging


load_dotenv()

logging.info("creating our agent...")
agent=create_agent(model="groq:qwen/qwen3.8-27b",
                   system_prompt=SYSTEM_CHEF_PROMPT,
                   tools=[web_search],)

logging.info("choosing our image...")
path=choose_image_file()
message=build_image_message(path,CHEF_PROMPT)


logging.info("invoking our agent....")
response=agent.invoke(
    {"messages":[message]}
)

print(response["messages"][-1].content)




