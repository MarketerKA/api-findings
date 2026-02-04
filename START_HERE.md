# 👋 START HERE!

## ⚡ Quick start in 3 steps

### Step 1: Activate virtual environment

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

After activation, you'll see `(venv)` at the beginning of your terminal prompt.

---

### Step 2: Check connection

```bash
python scripts/quick_test.py
```

You should see:
```
✅ Client created successfully
✅ Connection successful!
✅ All tests passed successfully!
```

---

### Step 3: Try searching

```bash
python scripts/search_keyword.py Governor
```

Result:
```
✅ Total found: 350 findings

📊 Statistics by severity level:
HIGH     :    44 findings
MEDIUM   :   111 findings
LOW      :   171 findings
GAS      :    24 findings
```

---

## 🎉 Done! What's next?

### 🔍 Try other search queries:

```bash
python scripts/search_keyword.py reentrancy
python scripts/search_keyword.py oracle
python scripts/search_keyword.py "flash loan"
python scripts/search_keyword.py "access control"
```

### 💬 Interactive mode:

```bash
python scripts/interactive_search.py
```

### 📚 Explore examples:

```bash
python examples/basic_usage.py
python examples/advanced_usage.py
```

### 📄 See finding format:

```bash
python scripts/simple_finding_example.py
python scripts/show_finding_format.py
```

---

## 📖 Documentation

| File | Description |
|------|-------------|
| [QUICKSTART.md](QUICKSTART.md) | Quick start with commands |
| [README.md](README.md) | Full project description |
| [docs/SETUP.md](docs/SETUP.md) | Installation and setup |
| [docs/USAGE.md](docs/USAGE.md) | Usage guide |
| [docs/FINDING_FORMAT.md](docs/FINDING_FORMAT.md) | Finding format guide |
| [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) | Project structure |

---

## 💻 Use in your code

Create file `my_script.py`:

```python
from src.solodit_client import SoloditClient

# Create client
client = SoloditClient()

# Search by keyword
data = client.search_findings(
    page=1,
    page_size=10,
    filters={"keywords": "reentrancy"}
)

# Print results
print(f"Found: {data['metadata']['totalResults']} findings\n")

for finding in data['findings']:
    print(f"[{finding['impact']}] {finding['title']}")
    print(f"  Firm: {finding.get('firm_name', 'N/A')}")
    print(f"  Quality: {finding['quality_score']}/5")
    print()
```

Run:
```bash
python my_script.py
```

---

## 🛑 When finished

When you're done:
```bash
deactivate
```

---

## ❓ Problems?

### Error: "Module not found"
**Solution:** Make sure venv is activated:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### Error: "API key not found"
**Solution:** Check `.env` file - it should contain:
```
API_KEY=sk_4db18175ab3aa879002b2406e5d2e3264fc64cf5b2ff4b341d940ba48e5b4413
```

### Error: "Rate limit exceeded"
**Solution:** Wait 60 seconds. Limit: 20 requests per minute.

---

## 🎯 Popular queries

| Query | Command |
|-------|---------|
| Governor contracts | `python scripts/search_keyword.py Governor` |
| Reentrancy attacks | `python scripts/search_keyword.py reentrancy` |
| Oracle issues | `python scripts/search_keyword.py oracle` |
| Flash loan attacks | `python scripts/search_keyword.py "flash loan"` |
| Access control | `python scripts/search_keyword.py "access control"` |
| Price manipulation | `python scripts/search_keyword.py "price manipulation"` |

---

## 📊 Project structure

```
Soldit-api/
├── src/              # Client source code
├── scripts/          # Ready-to-use scripts
├── examples/         # Usage examples
├── docs/             # Documentation
└── venv/             # Virtual environment
```

Details: [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md)

---

## 🚀 Ready to work!

Start with:
```bash
source venv/bin/activate && python scripts/quick_test.py
```

Good luck! 🎉
