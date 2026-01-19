# Product Sites MCP Service

A Model Context Protocol (MCP) service that identifies current deals and pricing information for products across reputable global retailers.

## Overview

This MCP service leverages AI-powered research to find verified purchasing options and real-time pricing for products. It searches across top-tier retailers, checks inventory status, and provides comprehensive procurement information to help users make informed purchasing decisions.

### Features

- **Multi-Retailer Search**: Checks pricing across Amazon, Best Buy, B&H, and other major retailers
- **Inventory Verification**: Confirms product availability and stock status in real-time
- **Price Normalization**: Reports MSRP vs. current best deals
- **Deal Detection**: Identifies active discount codes and limited-time bundles
- **Procurement Intelligence**: Provides shipping information and direct store links
- **Quality Filtering**: Ignores out-of-stock items and unknown third-party resellers with poor ratings

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python**: Version 3.8 or higher
- **pip**: Python package manager (comes with Python)
- **Google Cloud Setup**: A valid Google Generative AI API key (from Google AI Studio)

## Installation

### 1. Clone or Download the Repository

Navigate to the project directory:

```bash
cd mcp_productsites
```

### 2. Create a Virtual Environment (Recommended)

Creating a virtual environment keeps your project dependencies isolated:

#### On Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### On macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install all required packages from the requirements file:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root of the project directory:

```bash
# Windows PowerShell
New-Item -Path ".\.env" -ItemType File

# macOS/Linux
touch .env
```

Add your Google Generative AI API key to the `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

**To get your API key:**
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create or use an existing API key
3. Copy it and paste into your `.env` file

## Running the Service

### Start the MCP Server

Run the service using Python:

```bash
python mcp_productsites_server.py
```

The server will start and display:

```
🌐 MCP SSE Server: http://127.0.0.1:8002/sse
```

### Server Configuration

The service runs on:
- **Host**: 0.0.0.0 (accessible locally)
- **Port**: 8002
- **Transport**: Server-Sent Events (SSE)

### Using the Service

The service exposes a tool that can be called by MCP clients:

#### Get Today's Deals for a Product

Call the `get_todays_deals_for_product` function with a product name:

```python
result = await get_todays_deals_for_product("iPhone 16 Pro Max")
```

**Expected Output:**

The function returns a comprehensive procurement report including:
- **Product Information**: Brand, model, and key specifications
- **Pricing & Availability Table**: Retailer comparison with current prices, stock status, and shipping info
- **Procurement Notes**: Active discounts, bundle deals, and special offers

### Example Response Format

```
Product Information:
- Brand & Model: Apple iPhone 16 Pro Max
- Key Specs: 6.9" display, A18 Pro chip, 48MP camera, etc.

Pricing & Availability Table:
| Retailer | Current Price | Availability Status | Shipping Speed | Store Link |
| :--- | :--- | :--- | :--- | :--- |
| Amazon | $1,199.00 | In Stock | 1-2 days | [Link] |
| Best Buy | $1,199.00 | In Stock | Same-day | [Link] |
| B&H Photo | $1,189.00 | In Stock | 2-3 days | [Link] |

Procurement Note: B&H offering $10 discount for email signup. No active coupon codes at major retailers.
```

## Project Structure

```
mcp_productsites/
├── mcp_productsites_server.py    # Main MCP server
├── requirements.txt               # Python dependencies
├── .env                          # Environment variables (create this)
└── agent/
    └── productsites_agent.py     # AI agent configuration and logic
```

## Configuration Details

### Agent Configuration

The service uses a specialized e-commerce procurement agent with the following capabilities:

- **Model**: Gemini 2.0 Flash (fast, cost-effective)
- **Tools**: Google Search (real-time product availability)
- **Retailer Tiering**: Prioritizes established, reputable retailers
- **Quality Checks**: Filters unreliable third-party sellers

## Troubleshooting

### Issue: API Key Error

**Error**: `google.api_core.exceptions.InvalidArgument: Invalid API key`

**Solution**: 
- Verify your API key is correct and active in Google AI Studio
- Ensure the `.env` file is in the correct location
- Check that `python-dotenv` is installed: `pip install python-dotenv`

### Issue: Module Not Found

**Error**: `ModuleNotFoundError: No module named 'fastmcp'`

**Solution**:
- Make sure your virtual environment is activated
- Run `pip install -r requirements.txt` again
- Verify all packages installed correctly: `pip list`

### Issue: Port Already in Use

**Error**: `Address already in use` on port 8002

**Solution**:
- Either stop the other service using port 8002
- Or modify the port number in [mcp_productsites_server.py](mcp_productsites_server.py) (line with `port=8002`)

### Issue: No Results or Slow Response

**Solution**:
- Google Search may take 10-30 seconds for comprehensive results
- Ensure your internet connection is stable
- Try using a more specific product name (e.g., "iPhone 16 Pro Max 256GB" instead of just "iPhone")
- Check that the Google API service is accessible from your location

### Issue: Out-of-Stock Products Listed

**Note**: The agent filters obviously out-of-stock items, but some retailers may have delayed inventory updates. Always verify availability directly on the retailer's website.

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google Generative AI API key | Yes |

## Dependencies

The service requires the following Python packages:

| Package | Version | Purpose |
|---------|---------|---------|
| `fastmcp` | >=2.0.0 | MCP framework with SSE transport |
| `google-adk` | 1.20.0 | Google Agent Development Kit |
| `google-genai` | Latest | Google Generative AI API |
| `httpx` | >=0.27.0 | HTTP client library |
| `python-dotenv` | >=1.0.0 | Environment variable management |
| `pydantic` | Latest | Data validation |

## Development

### Customizing Retailer List

To modify which retailers are prioritized, edit [agent/productsites_agent.py](agent/productsites_agent.py):

- Modify the `instruction` parameter to include your preferred retailers
- Examples: "Costco", "Walmart", "Target", regional retailers

### Adjusting Search Behavior

- **Model**: Change the `model` parameter (default: `gemini-2.0-flash`)
- **Tools**: Modify search depth by adding/removing tools
- **Output Format**: Customize the response format in the `instruction` string

## Performance Notes

- Initial requests typically take 15-45 seconds as the agent searches multiple retailers
- Search time depends on retailer response times and internet speed
- Results are not cached; each request performs fresh research

## API Integration

### MCP Tool Definition

The service exposes the following tool to MCP clients:

```
Tool Name: get_todays_deals_for_product
Parameters:
  - trending_product (string): The name of the product to search for
Returns:
  - string: Comprehensive procurement report with pricing and availability
```

## Limitations

- **Real-time Data**: Prices and availability are current at time of search
- **Regional Availability**: Results may vary by geographic location
- **Retailer Coverage**: Focused on major English-language retailers
- **Product Specificity**: Requires specific product names for best results

## Support and Contributions

For issues, feature requests, or contributions, please refer to the main project README.

## License

This project is part of the ATC AI Event Agent Lab. Please refer to the root project license for more information.
