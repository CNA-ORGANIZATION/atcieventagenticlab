# 🎯 START HERE - Web UI Documentation Guide

Welcome to the ATC AI Event Agent Lab! 👋

This file will help you navigate the new Web UI documentation and get started quickly.

---

## ⚡ Super Quick Start (2 minutes)

```bash
# Make sure all MCP services are running, then:
cd trendagent
adk web
# Browser opens automatically to http://localhost:8000
# Done! Start chatting with the agent.
```

---

## 🎨 Choose Your Path

### 🏃 "I just want to use it" (15 minutes)
1. Run the command above
2. Read: `QUICK_REFERENCE.md` (keyboard shortcuts)
3. Start chatting!

### 📚 "I want to understand the Web UI" (30 minutes)
1. Read: `WEB_UI_QUICK_GUIDE.md`
2. Run: `adk web`
3. Explore all features
4. Read: `QUICK_REFERENCE.md` for pro tips

### 🏗️ "I want to understand the full system" (2 hours)
1. Read: Main `README.md` (architecture)
2. Read: `trendagent/README.md` (agent details)
3. Run the full system with all services
4. Explore both CLI and Web UI modes

### 👨‍💻 "I want to build my own system" (4+ hours)
1. Read: Main `README.md` (full guide)
2. Study: Developer Guide sections
3. Read: Individual service READMEs
4. Build: Your own MCP services and agents

---

## 📁 Documentation Files

| File | Time | Best For |
|------|------|----------|
| **QUICK_REFERENCE.md** | 5 min | Quick lookup |
| **WEB_UI_QUICK_GUIDE.md** | 15 min | Learning Web UI |
| **WEB_UI_UPDATES.md** | 10 min | Understanding changes |
| **README.md** | 45 min | Full project understanding |
| **trendagent/README.md** | 30 min | Agent-specific details |
| **DOCUMENTATION_INDEX.md** | 10 min | Finding documentation |
| **DOCUMENTATION_SUMMARY.md** | 10 min | Seeing all updates |
| **VISUAL_SUMMARY.md** | 5 min | Visual overview |
| **FILE_MANIFEST.md** | 5 min | What was created |

---

## 🚀 What's New: The `adk web` Command

### Old Way (Still Works)
```bash
python trend_agent.py
# Text-based terminal interface
```

### New Way (Recommended) ⭐
```bash
adk web
# Modern web interface opens automatically
```

### What's Different?

| Feature | CLI | Web UI |
|---------|-----|--------|
| Interface | Terminal | Browser |
| Formatting | Text only | Rich formatting |
| History | None | Persistent |
| Copy/Export | Manual | 1-click |
| Mobile | No | Yes |
| Professional | Basic | ✨ Modern |

---

## 🎯 Getting Started in 5 Steps

### Step 1: Run All MCP Services (Terminal 1-3)
```bash
# Terminal 1
cd mcp_trendscout
python mcp_trendsscout_server.py

# Terminal 2
cd mcp_productdetails
python mcp_productdetails_server.py

# Terminal 3
cd mcp_productsites
python mcp_productsites_server.py
```

### Step 2: Start Web UI (Terminal 4)
```bash
cd trendagent
adk web
```

### Step 3: Browser Opens
- Automatic: Your browser opens to `http://localhost:8000`
- Manual: Open `http://localhost:8000` if needed

### Step 4: Start Chatting
```
Type: "What's trending today?"
Get: Comprehensive response with trending products
```

### Step 5: Explore
- Try different questions
- Use keyboard shortcuts
- Copy responses
- Export conversations

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Send message |
| `Shift+Enter` | New line |
| `Ctrl+L` | Clear chat |
| `Ctrl+A` | Select all |

---

## 🆘 Quick Troubleshooting

### Q: Browser doesn't open
**A**: Go to `http://localhost:8000` manually

### Q: Web UI is blank
**A**: Refresh page (Ctrl+R) and check that all MCP services are running

### Q: "Connection refused"
**A**: Make sure all 3 MCP services are running first

### Q: Port 8000 in use
**A**: Use different port: `adk web --port 8001`

### Q: Slow first response
**A**: Normal - takes 30-60 seconds for initial research

---

## 📱 Accessing from Other Devices

**Same Computer:**
```
http://localhost:8000
```

**Other Computer on Network:**
```
Find your IP: ipconfig (Windows)
Then visit: http://192.168.1.100:8000 (your IP)
```

**Mobile on WiFi:**
```
Same as above - fully responsive design!
```

---

## 📚 Documentation Map

```
START HERE (This File)
│
├─ QUICK_REFERENCE.md ──────→ Keyboard shortcuts, quick commands
│
├─ WEB_UI_QUICK_GUIDE.md ───→ How to use Web UI, examples
│
├─ WEB_UI_UPDATES.md ───────→ What changed and why
│
├─ README.md ───────────────→ Full project architecture
│
└─ DOCUMENTATION_INDEX.md ──→ Find any documentation
```

---

## ✨ Key Features

### Chat Interface
- Clean, intuitive design
- Message history
- Real-time responses
- Easy input field

### Response Formatting
- Markdown support
- Tables with data
- Organized sections
- Copy button for each message

### User Actions
- Copy to clipboard
- Export conversation
- Clear chat
- Customize agent (if available)

---

## 🎓 Learning Outcomes

After using this, you'll know:
✅ How to start Web UI (`adk web`)
✅ How to interact with the agent
✅ All keyboard shortcuts
✅ How to access from other devices
✅ How to troubleshoot basic issues
✅ Difference between CLI and Web UI
✅ How to export conversations
✅ Full system architecture (if read README)
✅ How to build custom systems (if read Developer Guide)

---

## 🔗 Important Links

**API Key**: https://aistudio.google.com/app/apikey
**Main Guide**: `README.md`
**Agent Guide**: `trendagent/README.md`
**Quick Lookup**: `QUICK_REFERENCE.md`
**Web UI Help**: `WEB_UI_QUICK_GUIDE.md`
**All Docs**: `DOCUMENTATION_INDEX.md`

---

## 🎯 Example Queries

Try asking the agent:
```
"What's trending today?"
"Where can I buy it?"
"Show me the specifications"
"What's the best price?"
"Compare retailers"
"Tell me more details"
```

---

## 📊 What Happens Behind the Scenes

When you ask a question:
1. Agent receives your message
2. Calls TrendScout MCP service (find trends)
3. Calls Product Details MCP service (get specs)
4. Calls Product Sites MCP service (find prices)
5. Combines all information
6. Returns comprehensive answer

All in one conversation!

---

## ✅ Pre-Flight Checklist

Before starting, verify:
- [ ] Python 3.8+ installed
- [ ] Google API key obtained
- [ ] All MCP services can run
- [ ] Port 8000 available
- [ ] Browser installed
- [ ] Internet connection active

---

## 🚀 Ready to Start?

### Option 1: Just Try It
```bash
cd trendagent
adk web
# Browser opens, start asking questions!
```

### Option 2: Learn First
1. Read `QUICK_REFERENCE.md` (5 min)
2. Then run `adk web`
3. Reference shortcuts as needed

### Option 3: Full Understanding
1. Read `README.md` (45 min)
2. Read `trendagent/README.md` (30 min)
3. Run the system
4. Explore Web UI features

---

## 💡 Pro Tips

1. **Save Important Conversations**: Use Export button
2. **Share with Others**: Send them `http://[YOUR_IP]:8000`
3. **Use Natural Language**: The agent understands English well
4. **Ask Follow-ups**: It remembers context from previous questions
5. **Check Keyboard Shortcuts**: Many time-savers there

---

## 🎉 Welcome!

You now have everything you need to:
- Use the Web UI
- Interact with the agent
- Understand the system
- Troubleshoot issues
- Build your own system

**Choose a learning path above and get started!**

---

## 📞 Need Help?

| Issue | Solution |
|-------|----------|
| Quick question | `QUICK_REFERENCE.md` |
| How to use Web UI | `WEB_UI_QUICK_GUIDE.md` |
| Understanding changes | `WEB_UI_UPDATES.md` |
| System architecture | Main `README.md` |
| Agent details | `trendagent/README.md` |
| Find anything | `DOCUMENTATION_INDEX.md` |

---

## 🏆 Next Steps

1. ✅ Run `adk web`
2. ✅ Ask a question
3. ✅ Explore the interface
4. ✅ Try keyboard shortcuts
5. ✅ Read more documentation
6. ✅ Try accessing from another device
7. ✅ Export a conversation
8. ✅ Build your own system

---

**Happy exploring!** 🎊

Choose your learning path above and dive in. You've got this! 💪

---

*Last Updated: January 19, 2026*
*Status: ✅ Ready to Use*
