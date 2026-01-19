"""Interactive Google ADK Agent with MCP SSE - v1.20.0"""

import asyncio
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams
from google.genai import types

load_dotenv()

MCP_TRENDSCOUT_URL = "http://127.0.0.1:8001/sse"
MCP_PRODUCTDETAILS_URL = "http://127.0.0.1:8003/sse"
MCP_PRODCTSITES_URL = "http://127.0.0.1:8002/sse"


async def main():
    session_service = InMemorySessionService()
    
    session = await session_service.create_session(
        state={},
        app_name="weather_app",
        user_id="user1"
    )

    mcp_trendscout_toolset = McpToolset(
        connection_params=SseConnectionParams(url=MCP_TRENDSCOUT_URL)
    )
    
    mcp_productdetails_toolset = McpToolset(
        connection_params=SseConnectionParams(url=MCP_PRODUCTDETAILS_URL)
    )
    
    mcp_productsites_toolset = McpToolset(
        connection_params=SseConnectionParams(url=MCP_PRODCTSITES_URL)
    )
    
    

    agent = Agent(
        name="trending_alert_agent",
        model="gemini-2.0-flash",
        description="A trending alert assistant that provides current trending product, its details and sites selling this product.",
        instruction="""You are a helpful assistant to find current trending products and its details and sites selling this product. 
            Use the get_todays_product_trends tool for current trends.
            Use the get_product_details tool for product details.
            Use the get_todays_deals_for_product tool for sites selling products.""",
        tools=[mcp_trendscout_toolset, mcp_productdetails_toolset, mcp_productsites_toolset],
    )
    
    runner = Runner(
        app_name="weather_app",
        agent=agent,
        session_service=session_service,
    )

    print("🤖 Trending Alert Agent v1.20.0 (MCP SSE)")
    print("📡 Connected to:", MCP_TRENDSCOUT_URL)
    print("📡 Connected to:", MCP_PRODUCTDETAILS_URL)
    print("📡 Connected to:", MCP_PRODCTSITES_URL)
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("👤 You: ").strip()
        if user_input.lower() in ["quit", "exit", "q"]:
            break
        if not user_input:
            continue
        
        content = types.Content(
            role="user",
            parts=[types.Part(text=user_input)]
        )
        
        print("⏳ Processing...")
        
        events = runner.run_async(
            session_id=session.id,
            user_id=session.user_id,
            new_message=content
        )
        
        async for event in events:
            if hasattr(event, "content") and event.content:
                for part in event.content.parts:
                    if hasattr(part, "text") and part.text:
                        print(f"🤖 Assistant: {part.text}\n")
    
    await mcp_trendscout_toolset.close()
    await mcp_productdetails_toolset.close()
    await mcp_productsites_toolset.close()
    await session_service.close()
    print("👋 Goodbye!")

if __name__ == "__main__":
    asyncio.run(main())

