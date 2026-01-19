# Trending Alert Agent

An interactive AI agent that discovers trending consumer products and provides comprehensive information including detailed specs and current purchasing options across retailers.

## Overview

This agent orchestrates three specialized MCP (Model Context Protocol) services to deliver a complete product intelligence pipeline:

1. **TrendScout** - Identifies today's most trending products
2. **Product Details** - Retrieves comprehensive technical specifications and value propositions
3. **Product Sites** - Finds current pricing and deals across major retailers

The agent combines these services into a conversational interface, allowing you to discover trending products, understand their features, and find the best places to buy them—all in one interaction.

### Workflow

```
User Query
    ↓
Agent analyzes request and determines which MCP services to call
    ↓
TrendScout MCP → Returns trending product name
    ↓
Product Details MCP → Returns specs and analysis
    ↓
Product Sites MCP → Returns pricing and retailers
    ↓
Agent synthesizes findings and presents to user
```

## Prerequisites

Before running this agent, ensure you have:

### System Requirements
- **Python**: Version 3.8 or higher
- **pip**: Python package manager

### MCP Services Running
All three MCP services must be running before starting the agent:

1. **TrendScout Service** (Port 8001)
2. **Product Details Service** (Port 8003)
3. **Product Sites Service** (Port 8002)

See the individual service READMEs for setup instructions:
- [TrendScout Setup](../mcp_trendscout/README.md)
- [Product Details Setup](../mcp_productdetails/README.md)
- [Product Sites Setup](../mcp_productsites/README.md)

### API Keys
- **Google Generative AI API Key**: Required by the MCP services (configured in their `.env` files)

## Installation

### 1. Navigate to the Project Directory

```bash
cd trendagent
```

### 2. Create a Virtual Environment (Recommended)

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

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Optional)

If you need API keys for the agent itself, create a `.env` file:

```bash
# Windows PowerShell
New-Item -Path ".\.env" -ItemType File

# macOS/Linux
touch .env
```

Add any required variables:

```
GOOGLE_API_KEY=your_api_key_here
```

Note: The MCP services handle their own API key management via their respective `.env` files.

## Running the Agent

### Prerequisites Check

Before starting the agent, verify all MCP services are running:

#### Terminal 1 - TrendScout Service:
```bash
cd mcp_trendscout
python mcp_trendsscout_server.py
# Should display: 🌐 MCP SSE Server: http://127.0.0.1:8001/sse
```

#### Terminal 2 - Product Details Service:
```bash
cd mcp_productdetails
python mcp_productdetails_server.py
# Should display: 🌐 MCP SSE Server: http://127.0.0.1:8003/sse
```

#### Terminal 3 - Product Sites Service:
```bash
cd mcp_productsites
python mcp_productsites_server.py
# Should display: 🌐 MCP SSE Server: http://127.0.0.1:8002/sse
```

### Start the Agent

You have two options for running the agent:

#### Option A: Interactive Command-Line Mode

```bash
python trend_agent.py
```

You should see:

```
🤖 Trending Alert Agent v1.20.0 (MCP SSE)
📡 Connected to: http://127.0.0.1:8001/sse
📡 Connected to: http://127.0.0.1:8003/sse
📡 Connected to: http://127.0.0.1:8002/sse
Type 'quit' to exit

👤 You:
```

#### Option B: Web UI Mode (Recommended)

For a more user-friendly interface with a web-based UI:

```bash
adk web
```

This will:
1. Start the agent server
2. Automatically open your browser to `http://localhost:8000`
3. Provide a beautiful web interface for interacting with the agent
4. Display real-time responses and conversation history

**Advantages of Web UI Mode:**
- 🎨 Modern, user-friendly interface
- 💬 Chat-like conversation experience
- 📱 Works on any device with a browser
- 📊 Better visualization of responses
- 🔄 Session management built-in

**Advantages of Command-Line Mode:**
- ⚡ Lightweight and fast
- 🖥️ Direct control from terminal
- 🔧 Easier for scripting and automation

### Web UI Features

When running with `adk web`, you get a complete web-based interface:

**Chat Interface**
- Clean, intuitive chat-like design
- Message history visible in conversation
- Real-time streaming responses
- Easy input field for natural language queries

**Response Display**
- Formatted text with proper line breaks
- Tables for pricing and retailer information
- Organized sections (Executive Summary, Specs, etc.)
- Copy-to-clipboard functionality for responses

**Session Management**
- Persistent conversation history
- Clear conversation option
- Session state management
- Multi-turn conversations

**Browser Compatibility**
- Works in Chrome, Firefox, Safari, Edge
- Responsive design (mobile-friendly)
- No additional software required

**Accessing the Web UI**

After running `adk web`:
1. The browser automatically opens to `http://localhost:8000`
2. If not, manually navigate to that URL
3. You'll see a beautiful chat interface
4. Type your queries and press Send or Enter
5. Watch real-time responses appear in the chat

**Example Web UI Workflow:**
```
User Interface:
┌────────────────────────────────────────┐
│  🤖 Trending Alert Agent               │
├────────────────────────────────────────┤
│ Chat History:                           │
│                                        │
│ You: What's trending today?            │
│ Agent: The most trending product...   │
│                                        │
│ You: Where can I buy it?              │
│ Agent: You can purchase from...        │
│                                        │
├────────────────────────────────────────┤
│ [Message input field...        ] [Send]│
└────────────────────────────────────────┘
```

## Using the Agent

### Interactive Commands

The agent accepts natural language queries. Simply type your request and press Enter:

```
👤 You: What's trending today?
⏳ Processing...
🤖 Assistant: [Agent finds trending product and provides details]

👤 You: Where can I buy this product?
⏳ Processing...
🤖 Assistant: [Agent finds pricing and retailers]

👤 You: Tell me more about this product's specifications.
⏳ Processing...
🤖 Assistant: [Agent provides detailed specs and analysis]
```

### Example Interactions

#### Example 1: Discover Trending Products
```
👤 You: What's trending right now?

⏳ Processing...

🤖 Assistant: The most trending consumer product today is the Apple Vision Pro.
It's experiencing a 450% surge in search interest following recent availability 
announcements and celebrity endorsements on social media. This spatial computing 
device is generating significant buzz across tech enthusiast communities.
```

#### Example 2: Get Complete Product Information
```
👤 You: I want to know about the trending product - give me details and where to buy it.

⏳ Processing...

🤖 Assistant: 

TRENDING PRODUCT: Apple Vision Pro

EXECUTIVE SUMMARY:
Apple's Vision Pro is a spatial computing device that blends the physical and digital worlds. 
It represents a new category of personal computing.

KEY SPECIFICATIONS:
* Display: Dual micro-OLED displays, 4K resolution per eye
* Processor: Apple M2 chip
* Field of View: 110 degrees diagonal
* Battery Life: 2.5 hours

THE COMPETITIVE EDGE:
Superior display quality, seamless ecosystem integration, and revolutionary hand-eye tracking 
make it the most advanced spatial computer available.

BEST FOR: Early adopters, creative professionals, and tech enthusiasts interested in spatial computing.

WHERE TO BUY:
| Retailer | Price | Availability | Shipping |
| Apple Store | $3,499 | In Stock | 1-2 days |
| Best Buy | $3,499 | In Stock | Same-day |
| B&H Photo | $3,499 | Pre-order | 3-5 days |
```

#### Example 3: Specific Product Questions
```
👤 You: Is the trending product in stock anywhere right now?

⏳ Processing...

🤖 Assistant: Yes, the trending product is currently in stock at major retailers including 
Apple Store and Best Buy with immediate availability. B&H Photo has it on pre-order with 
delivery in 3-5 days.
```

### Exiting the Agent

To quit the interactive session, type:

```
👤 You: quit
👋 Goodbye!
```

Or use: `exit` or `q`

### Web UI Usage Guide

#### Starting the Web UI

```bash
adk web
```

Expected output:
```
Starting web server...
🚀 Server running at http://localhost:8000
📱 Opening browser...
```

Your default browser will automatically open to the web interface.

#### Web UI Layout

```
┌─────────────────────────────────────────────────────────────┐
│                  Trending Alert Agent                      │
├─────────────────────────────────────────────────────────────┤
│  Chat Area                                                  │
│  ┌───────────────────────────────────────────────────────┐ │
│  │ You: What's trending today?                      [copy] │
│  │                                                        │ │
│  │ Agent: The most trending product today is...     [copy] │
│  │ • Trend velocity: 450% spike                           │
│  │ • Primary signals: [sources listed]                    │
│  │                                                        │ │
│  │ You: Where can I buy it?                         [copy] │
│  │                                                        │ │
│  │ Agent: You can purchase from these retailers:    [copy] │
│  │ | Retailer | Price | Availability |                   │
│  │ | Amazon   | $X.XX | In Stock     |                   │
│  │                                                        │ │
│  └───────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│ Input: [Type your question here...                    [Send]│
│        [Clear chat]  [Export conversation]                 │
└─────────────────────────────────────────────────────────────┘
```

#### Key Web UI Features

**Message Input**
- Type naturally in the input field at the bottom
- Press Enter or click Send to submit
- Supports multi-line input (Shift+Enter for new line)

**Chat History**
- All messages and responses are preserved
- Click "Copy" to copy any message
- Scroll up to view earlier messages
- Use "Clear chat" to start fresh conversation

**Response Formatting**
- Markdown rendering for better readability
- Tables displayed with proper formatting
- Code blocks highlighted
- Links are clickable

**Quick Actions**
- **Copy**: Copy any message to clipboard
- **Export**: Download conversation as file
- **Clear**: Start a new conversation
- **Settings**: Configure agent behavior (if available)

#### Web UI Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Send message |
| `Shift+Enter` | New line in input |
| `Ctrl+L` / `Cmd+L` | Clear chat |
| `Ctrl+A` / `Cmd+A` | Select all (in input) |

#### Accessing from Other Devices

Once `adk web` is running:

**Same Computer (Default)**
- Open `http://localhost:8000`

**Other Devices on Network**
- Find your computer's IP address
- Open `http://[YOUR_IP]:8000` from other device
- Requires no special configuration

**Sharing the Web UI**
- Can be accessed by multiple users simultaneously
- Each user has independent session
- Share the URL with colleagues or clients

## Project Structure

```
trendagent/
├── trend_agent.py          # Main agent script
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (optional, create this)
└── README.md              # This file
```

## Configuration

### Service Endpoints

The agent connects to three MCP services. If your services run on different hosts or ports, modify [trend_agent.py](trend_agent.py):

```python
MCP_TRENDSCOUT_URL = "http://127.0.0.1:8001/sse"      # Trend discovery
MCP_PRODUCTDETAILS_URL = "http://127.0.0.1:8003/sse"   # Product analysis
MCP_PRODCTSITES_URL = "http://127.0.0.1:8002/sse"      # Retail pricing
```

### Agent Model Selection

To use a different AI model, edit [trend_agent.py](trend_agent.py) around line 43:

```python
agent = Agent(
    name="trending_alert_agent",
    model="gemini-2.0-flash",  # Change this to your preferred model
    ...
)
```

Available models:
- `gemini-2.0-flash` (default) - Fast, balanced performance
- `gemini-2.5-pro` - More comprehensive, slower responses

## Troubleshooting

### Issue: Connection Refused

**Error**: `Connection refused` when starting the agent

**Solution**:
- Ensure all three MCP services are running before starting the agent
- Verify the service URLs match what's configured in the agent
- Check that no services crashed; restart them if needed

### Issue: MCP Service Not Found

**Error**: `Could not connect to MCP service at [URL]`

**Solution**:
- Verify the service is running on the expected port
- Check if the port numbers have changed in the service configuration
- Update the URLs in [trend_agent.py](trend_agent.py) if needed

### Issue: Timeout During Processing

**Error**: Agent takes a long time or times out on first query

**Solution**:
- This is normal; initial requests can take 30-60 seconds
- The MCP services perform real-time research and web searches
- Subsequent queries are typically faster
- Check your internet connection stability

### Issue: Agent Crashes After Starting

**Error**: Agent starts but crashes when you type input

**Solution**:
- Ensure your virtual environment is activated
- Run `pip install -r requirements.txt` again
- Verify all MCP services are still running
- Check that Google API keys are valid in the MCP service `.env` files

### Issue: Module Import Errors

**Error**: `ModuleNotFoundError: No module named 'google.adk'`

**Solution**:
- Activate your virtual environment
- Run `pip install -r requirements.txt`
- Verify all packages installed: `pip list | grep google-adk`

### Web UI Specific Issues

#### Issue: Browser Doesn't Open Automatically

**Error**: `adk web` runs but browser window doesn't appear

**Solution**:
- Manually open `http://localhost:8000` in your browser
- Check if a different port was assigned (look at console output)
- Ensure your default browser is set properly

#### Issue: Web UI Times Out

**Error**: `Connection timeout` when making requests in web UI

**Solution**:
- Check that all MCP services are still running
- The first request may take 30-60 seconds
- Check browser console for error details
- Restart the `adk web` command if needed

#### Issue: Port 8000 Already in Use

**Error**: `Address already in use` when running `adk web`

**Solution**:
- Close any other applications using port 8000
- Or configure a different port via command line:
  ```bash
  adk web --port 8001
  ```

#### Issue: Web UI Shows Blank Chat

**Error**: Chat interface appears but no response to messages

**Solution**:
- Verify all three MCP services are running
- Check browser console (F12) for JavaScript errors
- Check the terminal running `adk web` for server errors
- Refresh the browser page (Ctrl+R or Cmd+R)

## Dependencies

The agent requires the following Python packages:

| Package | Version | Purpose |
|---------|---------|---------|
| `google-adk` | 1.20.0 | Google Agent Development Kit |
| `httpx` | >=0.27.0 | HTTP client for MCP communication |
| `python-dotenv` | >=1.0.0 | Environment variable management |

## Architecture

### Service Communication Flow

```
┌─────────────────────────┐
│   Trending Alert Agent  │
│    (This Program)       │
└────────┬────────────────┘
         │
    ┌────┴─────┬──────────┬────────────┐
    │           │          │            │
    ↓           ↓          ↓            ↓
┌────────┐ ┌──────────┐ ┌─────────┐ ┌──────────┐
│ Google │ │TrendScout│ │Product  │ │Product   │
│  ADK   │ │  MCP     │ │Details  │ │Sites MCP │
│        │ │Service   │ │MCP      │ │Service   │
│        │ │(8001)    │ │Service  │ │(8002)    │
│        │ │          │ │(8003)   │ │          │
└────────┘ └──────────┘ └─────────┘ └──────────┘
    ↓           ↓          ↓            ↓
    └───────────┬──────────┴────────────┘
                │
         ┌──────┴──────┐
         │              │
        ↓              ↓
   ┌──────────┐  ┌──────────┐
   │ Google   │  │ Web Search│
   │ Gemini   │  │ (via MCP) │
   │  Model   │  │           │
   └──────────┘  └──────────┘
```

## Development

### Customizing the Agent

To modify agent behavior, edit [trend_agent.py](trend_agent.py):

#### Change Agent Personality
```python
instruction="""You are a helpful assistant to find current trending products and its details and sites selling this product. 
    # Modify this instruction to change behavior
```

#### Add New MCP Services
```python
# Add new service connection
mcp_newservice_toolset = McpToolset(
    connection_params=SseConnectionParams(url="http://127.0.0.1:8004/sse")
)

# Add to agent tools list
tools=[mcp_trendscout_toolset, mcp_productdetails_toolset, mcp_productsites_toolset, mcp_newservice_toolset]
```

## Performance Notes

- **First Query**: 30-60 seconds (services perform real-time research)
- **Subsequent Queries**: 10-30 seconds (faster once services cache some data)
- **Memory Usage**: Moderate; agent maintains session state in memory
- **Concurrency**: Currently single-user interactive; modify code for multi-user support

## Use Cases

1. **Trend Research**: Discover what consumers are interested in right now
2. **Market Intelligence**: Monitor emerging product categories and trends
3. **Shopping Assistant**: Find trending products and compare prices
4. **Content Ideas**: Identify products for reviews, unboxings, or recommendations
5. **Business Analysis**: Track consumer interest for inventory decisions

## Limitations

- **Sequential Processing**: Queries are processed one at a time
- **Session State**: Agent state is in-memory only; sessions lost on restart
- **Single User**: Current implementation is for single-user interactive use
- **Real-time Dependency**: Requires all three MCP services to be running
- **API Rate Limits**: Subject to Google API rate limits configured in each service

## Advanced: Running Without Interactive Mode

To use the agent programmatically (non-interactive), modify [trend_agent.py](trend_agent.py):

```python
# Replace the while loop with:
user_input = "What's trending today?"

content = types.Content(
    role="user",
    parts=[types.Part(text=user_input)]
)

# Process the request...
```

## Support and Contributions

For issues, feature requests, or contributions, please refer to the main project README.

## License

This project is part of the ATC AI Event Agent Lab. Please refer to the root project license for more information.

## Quick Start Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] TrendScout MCP service running on port 8001
- [ ] Product Details MCP service running on port 8003
- [ ] Product Sites MCP service running on port 8002
- [ ] All MCP services have valid Google API keys in their `.env` files
- [ ] Run `python trend_agent.py` and type your questions!
