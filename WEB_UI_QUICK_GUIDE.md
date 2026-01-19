# Web UI Quick Guide - Visual Reference

## 🚀 Getting Started with Web UI

### Option 1: Quick Start (30 seconds)
```bash
# Assuming all MCP services are already running
cd trendagent
adk web
# Browser opens automatically to http://localhost:8000
```

### Option 2: Full Setup (from scratch)
```bash
# Terminal 1: TrendScout Service
cd mcp_trendscout
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
echo "GOOGLE_API_KEY=your_key_here" > .env
python mcp_trendsscout_server.py

# Terminal 2: Product Details Service
cd mcp_productdetails
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
echo "GOOGLE_API_KEY=your_key_here" > .env
python mcp_productdetails_server.py

# Terminal 3: Product Sites Service
cd mcp_productsites
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
echo "GOOGLE_API_KEY=your_key_here" > .env
python mcp_productsites_server.py

# Terminal 4: Web UI Agent
cd trendagent
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
adk web
# Browser opens to http://localhost:8000
```

---

## 🎨 Web UI Layout

```
╔═══════════════════════════════════════════════════════════════╗
║              🤖 Trending Alert Agent                          ║
║                  (adk web interface)                          ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  📋 CONVERSATION HISTORY                                     ║
║  ╔───────────────────────────────────────────────────────╗  ║
║  ║                                                       ║  ║
║  ║ You (10:45 AM):                                       ║  ║
║  ║ What's trending today?                                ║  ║
║  ║                                                   [Copy] ║  ║
║  ║                                                       ║  ║
║  ║ Agent (10:46 AM):                                     ║  ║
║  ║ The most trending consumer product today is...        ║  ║
║  ║ • Trend: Apple Vision Pro                            ║  ║
║  ║ • Velocity: 450% spike in search volume              ║  ║
║  ║ • Sources: Google Trends, Tech News, Social Media    ║  ║
║  ║                                                   [Copy] ║  ║
║  ║                                                       ║  ║
║  ║ You (10:47 AM):                                       ║  ║
║  ║ Where can I buy it?                                   ║  ║
║  ║                                                   [Copy] ║  ║
║  ║                                                       ║  ║
║  ║ Agent (10:48 AM):                                     ║  ║
║  ║ You can purchase the Apple Vision Pro from:           ║  ║
║  ║                                                       ║  ║
║  ║ │ Retailer    │ Price   │ Status   │ Shipping       │  ║
║  ║ ├─────────────┼─────────┼──────────┼────────────────┤  ║
║  ║ │ Apple Store │ $3,499  │ In Stock │ 1-2 days       │  ║
║  ║ │ Best Buy    │ $3,499  │ In Stock │ Same-day       │  ║
║  ║ │ B&H Photo   │ $3,489  │ Pre-ord  │ 3-5 days       │  ║
║  ║ │ Amazon      │ $3,499  │ In Stock │ 2-3 days       │  ║
║  ║                                                   [Copy] ║  ║
║  ║                                                       ║  ║
║  ║ ↓ (scroll for more)                                   ║  ║
║  ║                                                       ║  ║
║  ╚───────────────────────────────────────────────────────╝  ║
║                                                               ║
║  💬 INPUT & CONTROLS                                         ║
║  ┌───────────────────────────────────────────────────────┐  ║
║  │ Type your question here...        [Send] [⚙️ Settings] │  ║
║  └───────────────────────────────────────────────────────┘  ║
║                                                               ║
║  [📋 Clear Chat]  [📤 Export]  [🔄 New Session]            ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## ⌨️ How to Use

### Type Your Question
```
1. Click in the input field at the bottom
2. Type your question naturally
3. Press Enter or click [Send]
4. Watch the response appear in real-time
```

### Example Conversations

**Conversation 1: Discover Trends**
```
You: What's trending right now?

Agent: The most trending consumer product today is Apple Vision Pro.
It's experiencing a 450% surge in search interest following recent 
availability announcements and celebrity endorsements...
```

**Conversation 2: Get Details**
```
You: Tell me more about this product's specifications

Agent: EXECUTIVE SUMMARY:
Apple's Vision Pro is a spatial computing device...

KEY SPECIFICATIONS:
• Display: Dual micro-OLED, 4K per eye
• Processor: Apple M2 chip
• Field of View: 110 degrees diagonal
• Battery Life: 2.5 hours
```

**Conversation 3: Find Deals**
```
You: Where's the best deal on this product?

Agent: | Retailer  | Price   | Status   | Shipping |
      | B&H Photo | $3,489  | In Stock | 3-5 days |
      (Best price with $10 discount available)
```

---

## 🎯 Key Features

### Message Actions
- **[Copy]**: Copy any message to clipboard
- **[Export]**: Download entire conversation as text/PDF
- **[Clear]**: Start a fresh conversation
- **[Settings]**: Customize agent behavior

### Input Methods
| Method | Action |
|--------|--------|
| Type + Enter | Send message |
| Type + Shift+Enter | New line (multi-line input) |
| Click [Send] | Send message |

### Keyboard Shortcuts
| Shortcut | Action |
|----------|--------|
| `Enter` | Send message |
| `Shift+Enter` | New line in input |
| `Ctrl+L` | Clear chat history |
| `Ctrl+A` | Select all text in input |
| `Tab` | Auto-complete (if available) |

---

## 🌐 Accessing from Different Devices

### Same Computer
```
Open browser: http://localhost:8000
```

### Other Computers on Network
```
Find your IP: ipconfig (Windows) or ifconfig (Mac/Linux)
Open browser: http://[YOUR_IP]:8000

Example: http://192.168.1.100:8000
```

### Over Internet (with port forwarding)
```
Ask your network admin to forward external port → 8000
Then: http://[YOUR_EXTERNAL_IP]:8000
```

---

## ✨ Response Types You'll See

### Type 1: Simple Text Responses
```
The trending product today is Apple Vision Pro, which is 
experiencing massive interest with a 450% spike in search volume.
```

### Type 2: Formatted Lists
```
KEY SPECIFICATIONS:
• Display: Dual micro-OLED displays, 4K resolution per eye
• Processor: Apple M2 chip
• Memory: 8GB unified memory
• Storage: 256GB or 512GB SSD
```

### Type 3: Tables
```
| Retailer    | Price  | Availability | Shipping      |
|-------------|--------|--------------|---------------|
| Apple Store | $3,499 | In Stock     | 1-2 days      |
| Best Buy    | $3,499 | In Stock     | Same-day      |
| B&H Photo   | $3,489 | In Stock     | 3-5 days      |
```

### Type 4: Structured Analysis
```
PRODUCT INFORMATION:
Brand & Model: Apple Vision Pro
Key Specs: [details]

PRICING & AVAILABILITY:
[Comparison table]

PROCUREMENT NOTE:
B&H Photo offering $10 discount for email signup.
```

---

## 🆘 Quick Troubleshooting

### Q: Browser doesn't open automatically
**A**: Manually go to `http://localhost:8000`

### Q: Connection times out
**A**: 
1. Check that all MCP services are running
2. Wait 30-60 seconds (first request is slower)
3. Refresh the page (Ctrl+R)

### Q: Web UI is blank
**A**:
1. Open browser console (F12)
2. Check for JavaScript errors
3. Refresh page
4. Restart `adk web` if still blank

### Q: Port 8000 already in use
**A**: Use different port:
```bash
adk web --port 8001
# Then open http://localhost:8001
```

### Q: Responses are slow
**A**: This is normal - the agent performs web research:
- 1st response: 30-60 seconds
- Subsequent: 10-30 seconds

---

## 📊 Comparison: CLI vs Web UI

### CLI Mode (Terminal)
```bash
$ python trend_agent.py
🤖 Agent connected
Type 'quit' to exit

👤 You: What's trending?
⏳ Processing...
🤖 Assistant: [response here]
```
- ✅ Direct terminal access
- ✅ No browser required
- ❌ Plain text only
- ❌ No persistent history

### Web UI Mode (Browser)
```
🤖 Trending Alert Agent
[Chat interface with rich formatting]
User: What's trending?
Agent: [formatted response with tables/lists]
```
- ✅ Rich formatting
- ✅ Persistent history
- ✅ Mobile friendly
- ✅ Professional UI
- ❌ Requires browser

---

## 🚀 Pro Tips

### Tip 1: Ask Follow-up Questions
```
You: What's trending?
Agent: [Apple Vision Pro...]

You: How much does it cost?
Agent: [pricing information...]

You: Where can I get the best deal?
Agent: [comparisons...]
```

### Tip 2: Export Conversations
```
Click [📤 Export] to save conversation as:
- PDF report
- Text file
- JSON data
```

### Tip 3: Share Conversations
```
1. Export conversation
2. Send to colleagues/clients
3. They can read your research
```

### Tip 4: Use Natural Language
```
Good: "I want to know about the trending product"
Good: "Where's the cheapest place to buy this?"
Good: "Show me the specifications"

The agent understands natural English!
```

---

## 📱 Mobile Access

The Web UI is **fully responsive** and works great on mobile:

### From Phone on Same WiFi
1. Get computer IP: `ipconfig` (Windows)
2. Open `http://[IP]:8000` in phone browser
3. Chat as if on desktop
4. Perfect for demonstrations!

### From Tablet
- Same process as phone
- Larger screen = easier to read responses
- Touch-friendly interface

---

## 🔐 Security Notes

- Web UI runs on localhost by default (your computer only)
- To access from network, make sure to configure firewall
- Don't expose to the internet without proper authentication
- Session data is in-memory (lost on restart)

---

## 📞 Getting Help

### Issue: Commands not working
- Verify all MCP services running
- Check ports 8001, 8002, 8003, 8000 are available
- Restart the agent

### Issue: API errors
- Verify `GOOGLE_API_KEY` in all `.env` files
- Get new key from: https://aistudio.google.com/app/apikey

### Issue: Still stuck?
- Read the main `README.md` in project root
- Check individual service READMEs
- See troubleshooting sections

---

## 🎓 Learning Path

1. **First Time**: Run `adk web` and ask simple questions
2. **Explore**: Try different types of questions
3. **Advanced**: Ask complex questions with multiple parts
4. **Master**: Build your own MCP services and agents

---

**Enjoy exploring the Web UI! 🎉**

For detailed information, see:
- Main README: `README.md`
- Agent README: `trendagent/README.md`
- Web UI Guide: See "Web UI Usage Guide" in agent README
