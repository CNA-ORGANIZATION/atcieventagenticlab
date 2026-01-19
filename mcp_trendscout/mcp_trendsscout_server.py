from fastmcp import FastMCP
import agent.trends_scout_agent as trends_scout_agent


import asyncio
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams
from google.genai import types


mcp = FastMCP("TrendScout MCP")

load_dotenv()
session_service = InMemorySessionService()
agent: Agent = trends_scout_agent.scout_agent

app_name = "trend_scout_app"

async def _get_todays_product_trends() -> str:
    runner = Runner(
        app_name=app_name,
        agent=agent,
        session_service=session_service,
    )

    session = await session_service.create_session(
        state={},
        app_name=app_name,
        user_id="user1"
    )
    
    content = types.Content(
        role="user",
        parts=[types.Part(text="get todays most trending consumer product")],
    )

    events_async = runner.run_async(session_id=session.id,
            user_id=session.user_id,
            new_message=content
        )
    result = ""
    async for event in events_async:
        if event.is_final_response():
            result = event.content.parts[0].text
            print("➡️ Agent Response:\n", result)
    return result

@mcp.tool()
async def get_todays_product_trends() -> str:
    """Get today's most trending consumer product."""
    return await _get_todays_product_trends()

if __name__ == "__main__":
#    asyncio.run(_get_todays_product_trends())
    print("🌐 MCP SSE Server: http://127.0.0.1:8001/sse")
    mcp.run(transport="sse", host="0.0.0.0", port=8001)
