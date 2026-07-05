from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import asyncio
load_dotenv()
llm= ChatOllama(
   model="gpt-oss:20b"
)
async def main():
    print("Hello from langchainmcp")

if __name__ == "__main__":
    asyncio.run(main())