from pydantic_ai import Agent
from dotenv import load_dotenv
load_dotenv()

agent = Agent(model="groq:llama-3.3-70b-specdec")
