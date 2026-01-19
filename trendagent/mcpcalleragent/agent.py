"""Interactive Google ADK Agent with MCP SSE - v1.20.0"""
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams

MCP_TRENDSCOUT_URL = "http://127.0.0.1:8001/sse"
MCP_PRODUCTDETAILS_URL = "http://127.0.0.1:8003/sse"
MCP_PRODCTSITES_URL = "http://127.0.0.1:8002/sse"


root_agent = Agent(
    name="trending_alert_agent",
    model="gemini-2.0-flash",
    description="A trending alert assistant that provides current trending product, its details and sites selling this product.",
    instruction="""You are a helpful assistant to find current trending products and its details and sites selling this product. 
        Use the get_todays_product_trends tool for current trends.
        Use the get_product_details tool for product details.
        Use the get_todays_deals_for_product tool for sites selling products.""",
    tools=[
        McpToolset(
            connection_params=SseConnectionParams(url=MCP_TRENDSCOUT_URL)
        ),
        McpToolset(
            connection_params=SseConnectionParams(url=MCP_PRODUCTDETAILS_URL)
        ),
        McpToolset(
            connection_params=SseConnectionParams(url=MCP_PRODCTSITES_URL)
        )
    ],
)
