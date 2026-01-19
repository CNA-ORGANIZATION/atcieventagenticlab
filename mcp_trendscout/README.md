# TrendScout MCP Service

A Model Context Protocol (MCP) service that identifies the most impactful trending consumer products in real-time using AI-powered trend intelligence.

## Overview

This MCP service leverages Google's Gemini 2.5 Pro model to discover what's trending globally right now. It cross-references multiple authority sources (Google Trends, tech news, social media), filters out evergreen products, and identifies consumer products with the highest growth velocity—perfect for staying ahead of market movements.

### Features

- **Real-Time Trend Detection**: Monitors Google Trends, tech news, and social platforms for emerging trends
- **Multi-Source Verification**: Cross-references at least three authority clusters to confirm trends
- **Growth Velocity Analysis**: Identifies products with 200%+ search volume spikes
- **Smart Filtering**: Ignores evergreen products, focuses on new releases and sudden surges
- **Global Coverage**: Tracks trending products across international markets
- **High-Performance Model**: Uses Gemini 2.5 Pro for comprehensive, accurate analysis

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python**: Version 3.8 or higher
- **pip**: Python package manager (comes with Python)
- **Google Cloud Setup**: A valid Google Generative AI API key (from Google AI Studio)

## Installation

### 1. Clone or Download the Repository

Navigate to the project directory:

```bash
cd mcp_trendscout
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
python mcp_trendsscout_server.py
```

The server will start and display:

```
🌐 MCP SSE Server: http://127.0.0.1:8001/sse
```

### Server Configuration

The service runs on:
- **Host**: 0.0.0.0 (accessible locally)
- **Port**: 8001
- **Transport**: Server-Sent Events (SSE)

### Using the Service

The service exposes a tool that can be called by MCP clients:

#### Get Today's Product Trends

Call the `get_todays_product_trends` function to discover what's trending right now:

```python
result = await get_todays_product_trends()
```

**Expected Output:**

The function returns a comprehensive trend report with:
- **PRODUCT_NAME**: The exact name of the trending product
- **TREND_VELOCITY**: Explanation of the search/social spike
- **PRIMARY_SIGNALS**: 2-3 specific sources confirming the trend

### Example Response Format

```
PRODUCT_NAME: Apple Vision Pro
TREND_VELOCITY: 450% spike in search volume over last 24 hours following surprise availability announcement and celebrity endorsements across TikTok and YouTube.
PRIMARY_SIGNALS:
- Google Trends: "Apple Vision Pro" ranked #1 globally in Consumer Electronics category
- Social Media: 250K+ viral posts on TikTok with #AppleVisionPro
- Tech News: Coverage from The Verge, WIRED, and MacRumors within last 6 hours
```

## Project Structure

```
mcp_trendscout/
├── mcp_trendsscout_server.py    # Main MCP server
├── requirements.txt              # Python dependencies
├── .env                         # Environment variables (create this)
└── agent/
    └── trends_scout_agent.py    # AI agent configuration and logic
```

## Configuration Details

### Agent Configuration

The service uses an advanced trend intelligence agent with the following specifications:

- **Model**: Gemini 2.5 Pro (most advanced, comprehensive analysis)
- **Tools**: Google Search (real-time trend detection)
- **Output Key**: `trending_product` (structured response format)
- **Velocity Threshold**: 200%+ search volume growth
- **Source Diversity**: Cross-references multiple authority clusters

### Understanding Trend Velocity

The agent prioritizes products based on **velocity**—the speed and scale of trend growth:

- **Low Velocity**: Slow, gradual growth (ignored)
- **Medium Velocity**: 50-200% growth (considered)
- **High Velocity**: 200%+ growth (prioritized)
- **Viral**: Exponential growth across multiple platforms (highest priority)

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

**Error**: `Address already in use` on port 8001

**Solution**:
- Either stop the other service using port 8001
- Or modify the port number in [mcp_trendsscout_server.py](mcp_trendsscout_server.py) (line with `port=8001`)

### Issue: No Trends Found

**Solution**:
- This is rare but can happen if there's unusual global internet disruption
- Try again after a few minutes
- Ensure your internet connection is stable
- Check that the Google API service is accessible from your location

### Issue: Response Takes Long Time

**Solution**:
- Initial requests can take 30-60 seconds as the agent searches multiple platforms
- This is normal—the Gemini 2.5 Pro model performs comprehensive research
- Subsequent requests may use cached insights if running continuously

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

### Customizing Trend Detection

To modify trend detection behavior, edit [agent/trends_scout_agent.py](agent/trends_scout_agent.py):

- **Velocity Threshold**: Modify the `200%+` threshold in the instruction
- **Source Clusters**: Add or change authority sources (e.g., Reddit, industry-specific sites)
- **Product Category**: Customize the `instruction` to focus on specific product categories (tech, fashion, lifestyle, etc.)

### Adjusting Model and Tools

- **Model**: Change to `gemini-2.0-flash` for faster but less comprehensive results
- **Tools**: Add additional tools like YouTube API for social media trend detection
- **Output Format**: Customize the response format in the `instruction` string

### Example: Focus on Tech Products Only

```python
# In trends_scout_agent.py, modify the instruction:
instruction="""...[your instruction]...
### CATEGORY FILTER
Only consider products in these categories: Consumer Electronics, Software, Gadgets, AI Tools.
Ignore fashion, food, and entertainment products.
```

## Performance Characteristics

- **Response Time**: 30-60 seconds (comprehensive multi-source research)
- **Accuracy**: High (Gemini 2.5 Pro with multi-source verification)
- **Update Frequency**: Best used hourly or every few hours for new trend discovery
- **Global Coverage**: English-language sources primarily, with some international coverage

## Use Cases

1. **E-Commerce**: Identify products to feature and stock based on real-time demand
2. **Content Creators**: Discover trending products for reviews, unboxings, and recommendations
3. **Marketers**: Find emerging trends for campaign planning and audience engagement
4. **Investors**: Monitor consumer product trends for investment opportunities
5. **Retailers**: Adjust inventory based on current market trends

## API Integration

### MCP Tool Definition

The service exposes the following tool to MCP clients:

```
Tool Name: get_todays_product_trends
Parameters: None
Returns:
  - string: Comprehensive trend report including product name, velocity, and source signals
```

## Limitations

- **Language**: Primarily English-language sources and products
- **Recency**: Trends are from the last 24 hours; older trends are filtered out
- **Product Specificity**: Focuses on consumer products; B2B or enterprise products may not appear
- **Category**: Mainstream consumer products; niche items may be underrepresented
- **Geographic**: Results reflect global trends; regional trends require custom configuration

## Performance Notes

- Uses Gemini 2.5 Pro for the most comprehensive trend analysis
- Higher latency (30-60s) but more accurate than faster models
- Consider caching results if called frequently within short time windows
- Google Trends data updates every 6 hours; search volume data is real-time

## Support and Contributions

For issues, feature requests, or contributions, please refer to the main project README.

## License

This project is part of the ATC AI Event Agent Lab. Please refer to the root project license for more information.
