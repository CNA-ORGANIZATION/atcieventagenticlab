from fastmcp import FastMCP
import agent.productsites_agent as productsites_agent


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
agent: Agent = productsites_agent.deal_agent

app_name = "trending_product_deal_app"

async def _get_todays_deals_for_product(trending_product: str) -> str:
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
        parts=[types.Part(text=f"get product deals for {trending_product}")],
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
async def get_todays_deals_for_product(trending_product: str) -> str:
    """Get deals for a given trending product."""
    return await _get_todays_deals_for_product(trending_product)

if __name__ == "__main__":
#    asyncio.run(_get_todays_product_trends())
    print("🌐 MCP SSE Server: http://127.0.0.1:8002/sse")
    mcp.run(transport="sse", host="0.0.0.0", port=8002)
