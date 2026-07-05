import asyncio
from dotenv import load_dotenv
load_dotenv()
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_ollama import ChatOllama
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
llm= ChatOllama(
   model="gpt-oss:20b"
)
stdio_server_params  = StdioServerParameters(
    command="python",
    args=["C:/Users/MANIKANTA/OneDrive/Documents/coding/mcp/servers/math_server.py"]
)
async def main():
    print("Hello from mcp")
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read, write) as session:

            # This line is what the instructor is typing
            await session.initialize()

            # Load MCP tools
            tools = await load_mcp_tools(session)

            # Create LangGraph ReAct Agent
            agent = create_react_agent(llm, tools)

            response = await agent.ainvoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": "What is 20 * 50?"
                        }
                    ]
                }
            )

            print(response)
if __name__ == "__main__":
    asyncio.run(main())