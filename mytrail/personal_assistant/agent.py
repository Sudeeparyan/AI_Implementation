from google.adk.agents import Agent

root_agent = Agent(
    name = "personal_assistant",
    model = "gemini-2.0-flash",
    description= "A personal assistant agent who works for Sudeep Aryan.",
    instruction="You are a personal assistant for Sudeep Aryan. He is a software engineer living in Ireland"
)