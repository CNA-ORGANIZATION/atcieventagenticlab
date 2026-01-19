# Product Details MCP Service

A Model Context Protocol (MCP) service that provides comprehensive product information and analysis using AI-powered research and synthesis.

## Overview

This MCP service leverages Google's Generative AI and web search capabilities to deliver detailed product specifications, competitive analysis, and value propositions. It's designed to work with AI agents that need to gather and analyze product information on demand.

### Features

- **Comprehensive Product Research**: Automatically searches for official specifications and detailed product information
- **Expert Analysis**: Synthesizes information from professional reviews and industry sources
- **Competitive Edge Analysis**: Identifies key differentiators compared to competing products
- **Value Proposition**: Provides clear guidance on target users and ideal use cases
- **AI-Powered**: Built on Google's Gemini 2.0 Flash model for fast, accurate analysis

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python**: Version 3.8 or higher
- **pip**: Python package manager (comes with Python)
- **Google Cloud Setup**: A valid Google Generative AI API key (from Google AI Studio)

## Installation

### 1. Clone or Download the Repository

Navigate to the project directory:

```bash
cd mcp_productdetails
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
python mcp_productdetails_server.py
```

You should see output indicating the server is running.

### Using the Service

The service exposes a primary function that can be called by agents:

#### Get Product Details

Call the `_get_product_details` function with a product name:

```python
result = await _get_product_details("iPhone 16 Pro Max")
```

**Expected Output:**

The function returns a comprehensive analysis including:
- **Executive Summary**: 2-sentence high-level overview
- **Key Specifications**: Technical specs and features
- **Competitive Edge**: What makes this product stand out
- **Best For**: Target audience and ideal use cases

### Example Response Format

```
Executive Summary: [2-sentence overview]

Key Specifications:
* Display: [Details]
* Processor: [Details]
* Battery: [Details]
* Camera: [Details]

The Competitive Edge: [Analysis of competitive advantages]

Best For: [Target users and use cases]
```

## Project Structure

```
mcp_productdetails/
├── mcp_productdetails_server.py    # Main MCP server
├── requirements.txt                 # Python dependencies
├── .env                            # Environment variables (create this)
└── agent/
    └── productdetails_agent.py     # AI agent configuration and logic
```

## Troubleshooting

### Issue: API Key Error

**Error**: `google.api_core.exceptions.InvalidArgument: Invalid API key`

**Solution**: 
- Verify your API key is correct and active in Google AI Studio
- Ensure the `.env` file is in the correct location
- Check that `python-dotenv` is installed

### Issue: Module Not Found

**Error**: `ModuleNotFoundError: No module named 'fastmcp'`

**Solution**:
- Make sure your virtual environment is activated
- Run `pip install -r requirements.txt` again
- Verify the requirements file has all necessary packages

### Issue: Timeout or Slow Response

**Solution**:
- The service may be performing web searches; this can take 10-30 seconds
- Ensure your internet connection is stable
- Check that the Google API service is accessible from your location

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google Generative AI API key | Yes |

## Dependencies

The service requires the following Python packages:

| Package | Version | Purpose |
|---------|---------|---------|
| `fastmcp` | >=2.0.0 | MCP framework |
| `google-adk` | 1.20.0 | Google Agent Development Kit |
| `google-genai` | Latest | Google Generative AI API |
| `httpx` | >=0.27.0 | HTTP client library |
| `python-dotenv` | >=1.0.0 | Environment variable management |
| `pydantic` | Latest | Data validation |

## Development

### Modifying the Agent

To customize product analysis behavior, edit [agent/productdetails_agent.py](agent/productdetails_agent.py):

- **Model**: Change the `model` parameter (default: `gemini-2.0-flash`)
- **Instructions**: Modify the `instruction` string to change analysis focus
- **Tools**: Add or remove tools used by the agent (e.g., `google_search`)

## Performance Notes

- Initial requests may take 10-30 seconds as the agent performs research
- Subsequent requests for similar products may benefit from caching (if implemented)
- The service uses Gemini 2.0 Flash for fast, cost-effective responses

## Support and Contributions

For issues, feature requests, or contributions, please refer to the main project README.

## License

This project is part of the ATC AI Event Agent Lab. Please refer to the root project license for more information.
