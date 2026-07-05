import asyncio
from dotenv import load_dotenv
load_dotenv()
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_ollama import ChatOllama
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
llm= ChatOllama(
   model="gpt-oss:20b"
)
stdio_server_params  = StdioServerParameters(
    command="python",
    args=["C:/Users/MANIKANTA/OneDrive/Documents/coding/mcp/servers/math_server.py"]
)
async def main():
    print("Hello from mcp")

if __name__ == "__main__":
    asyncio.run(main())