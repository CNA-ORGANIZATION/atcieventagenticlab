# Quick Reference Card - Web UI

## 🎯 One-Command Setup

```bash
# From project root
cd trendagent
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt
adk web
```

**Output**: Browser opens to `http://localhost:8000`

---

## 📋 Running Modes

### Command-Line (Terminal)
```bash
python trend_agent.py
# Interact: Type queries, get text responses
# Exit: Type 'quit'
```

### Web UI (Browser) ⭐ Recommended
```bash
adk web
# Interact: Chat interface with formatting
# Exit: Close browser or Ctrl+C
```

---

## ⌨️ Keyboard Shortcuts

| Windows/Linux | macOS | Action |
|---|---|---|
| `Enter` | `Enter` | Send message |
| `Shift+Enter` | `Shift+Enter` | New line |
| `Ctrl+L` | `Cmd+L` | Clear chat |
| `Ctrl+A` | `Cmd+A` | Select all |

---

## 🌐 Access URLs

| Location | URL |
|----------|-----|
| Same computer | `http://localhost:8000` |
| Other device (example) | `http://192.168.1.100:8000` |
| Different port | `http://localhost:8001` |

---

## 📊 Feature Comparison

| Feature | CLI | Web UI |
|---------|-----|--------|
| Speed | ⚡ Fast | ⚡⚡ Fast |
| UI | 📝 Text | 🎨 Modern |
| Mobile | ❌ No | ✅ Yes |
| Tables | ❌ No | ✅ Yes |
| History | ❌ No | ✅ Yes |
| Copy | ❌ No | ✅ Yes |

---

## 🛠️ Troubleshooting Quick Fixes

| Issue | Solution |
|-------|----------|
| Browser doesn't open | Manually: `http://localhost:8000` |
| Slow first response | Normal - takes 30-60 seconds |
| Port 8000 in use | `adk web --port 8001` |
| Connection error | Verify MCP services running |
| Blank page | Refresh browser (Ctrl+R) |

---

## 📝 Example Queries

```
"What's trending today?"
"Where can I buy it?"
"Show me the specifications"
"What's the best deal?"
"Compare prices across retailers"
"Tell me more about this product"
```

---

## 🔧 Service Ports

| Service | Port | Command |
|---------|------|---------|
| TrendScout MCP | 8001 | `python mcp_trendsscout_server.py` |
| Product Sites MCP | 8002 | `python mcp_productsites_server.py` |
| Product Details MCP | 8003 | `python mcp_productdetails_server.py` |
| Web UI Agent | 8000 | `adk web` |

---

## 📦 Required Files

For Web UI to work, need all running:

```
✓ mcp_trendscout/    (Port 8001)
✓ mcp_productdetails/  (Port 8003)
✓ mcp_productsites/    (Port 8002)
✓ trendagent/          (Port 8000) ← Run: adk web
```

---

## 🚀 Quick Start in 5 Steps

1. Open 4 terminals
2. Terminal 1: `cd mcp_trendscout && python mcp_trendsscout_server.py`
3. Terminal 2: `cd mcp_productdetails && python mcp_productdetails_server.py`
4. Terminal 3: `cd mcp_productsites && python mcp_productsites_server.py`
5. Terminal 4: `cd trendagent && adk web` ← Browser opens automatically

**Done!** Start chatting with the agent.

---

## 💡 Pro Tips

```
1. Copy responses: Click [Copy] next to any message
2. Export chat: Click [📤 Export] to save conversation
3. Multi-line: Use Shift+Enter for line breaks
4. Ask follow-ups: Chat continues with full context
5. Network: Share http://[YOUR_IP]:8000 with others
```

---

## 🔗 Important Links

- **Main README**: `README.md`
- **Agent Docs**: `trendagent/README.md`
- **Web UI Guide**: In agent README under "Web UI Usage Guide"
- **API Key**: https://aistudio.google.com/app/apikey

---

## ⏱️ Timing Expectations

| Action | Time |
|--------|------|
| `adk web` startup | 2-3 seconds |
| Browser opening | 2-3 seconds |
| 1st query response | 30-60 seconds |
| 2nd+ query response | 10-30 seconds |
| Copy to clipboard | Instant |

---

## 🎨 Web UI Layout Snapshot

```
┌─────────────────────────────────────┐
│    Trending Alert Agent (adk web)   │
├─────────────────────────────────────┤
│                                     │
│  Chat History (scrollable)          │
│  [Your messages and responses]       │
│                                     │
│  Input: [Type here...] [Send] [More]│
│                                     │
└─────────────────────────────────────┘
```

---

## 📱 Mobile Browser Compatibility

| Browser | Status | Notes |
|---------|--------|-------|
| Chrome | ✅ Works | Recommended |
| Firefox | ✅ Works | Good |
| Safari | ✅ Works | Works on iOS |
| Edge | ✅ Works | Works |

---

## 🆚 CLI vs Web UI Decision Tree

```
Do you want...
├─ Simple/Fast terminal → CLI: python trend_agent.py
├─ Rich formatting/UI → Web UI: adk web ⭐
├─ Mobile access → Web UI: adk web ⭐
├─ Easy sharing → Web UI: adk web ⭐
├─ Scripting → CLI: python trend_agent.py
└─ Automation → CLI: python trend_agent.py
```

**Recommendation**: 90% use cases → **adk web** 🎯

---

## 📞 Common Questions

**Q: Can both CLI and Web UI run simultaneously?**
A: Yes! They connect to same agent. Run in different terminals.

**Q: Do I lose chat history if page refreshes?**
A: No! Web UI maintains history until you clear it.

**Q: Can multiple people use Web UI together?**
A: Yes! Share URL or IP:port with others.

**Q: Is Web UI secure for internet access?**
A: Only localhost by default. Use firewall for network.

**Q: Do I need a Google account?**
A: Just an API key from: https://aistudio.google.com/app/apikey

---

## ✅ Checklist Before Starting

- [ ] All MCP services running
- [ ] Python 3.8+ installed
- [ ] Dependencies: `pip install -r requirements.txt`
- [ ] Google API key in `.env` files
- [ ] Port 8000 available (or use `--port`)
- [ ] Browser installed and working

**Ready?** Run: `adk web` 🚀

---

## 🎓 Next Steps

1. ✅ Get Web UI running (`adk web`)
2. ✅ Ask some example questions
3. ✅ Explore the formatting and features
4. ✅ Try accessing from another device
5. ✅ Read full documentation for advanced features

---

**Status**: Ready to Use ✨
**Version**: 1.0
**Last Updated**: January 19, 2026
