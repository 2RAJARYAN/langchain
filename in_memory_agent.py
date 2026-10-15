from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver


load_dotenv()

agent=create_agent(model="groq:openai/gpt-oss-120b",
                   checkpointer=InMemorySaver(),
                   )


# config will tell agent this is conversation we taking about
config={"configurable":{"thread_id":"1"}}


response=agent.invoke(
    {"messages":[HumanMessage(content="my favorite color is yellow.")]},
    config
)

print(response["messages"][-1].content)

response=agent.invoke(
    {"messages":[HumanMessage(content="what is my favorite color?")]},
    config
)

print(response["messages"][-1].content)


