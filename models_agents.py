from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.messages import HumanMessage,AIMessage

load_dotenv()

# model = init_chat_model(
#     model="groq:openai/gpt-oss-120b",
#     temperature=0  # 0 to 1 from least creative to most creative 
# )
# agent=create_agent(model=model)
agent=create_agent(model="groq:openai/gpt-oss-120b")

for token, metadata in agent.stream(
    {"messages":[HumanMessage(content="what is the capital of india? "),
                 AIMessage(content="The capital of India is **New Delhi**."),
                 HumanMessage(content="tell me more about it .")]},
                 stream_mode="messages"
):
    if token.content:
        print(token.content,end="",flush=True)

"""
response=agent.invoke(
    {"messages":[HumanMessage(content="what is the capital of india? "),
                 AIMessage(content="The capital of India is **New Delhi**."),
                 HumanMessage(content="tell me more about it in less than 20 words.")]}
)
# response=model.invoke("what is the capital of india? and what special about that in 30 words.")
print(response["messages"][-1].content)

# print(response["messages"])
"""
