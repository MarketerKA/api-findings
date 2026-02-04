# 🚀 Quick Start

## Activate virtual environment

### Linux/Mac:
```bash
source venv/bin/activate
```

### Windows:
```bash
venv\Scripts\activate
```

After activation, you'll see `(venv)` at the beginning of your prompt.

---

## 🧪 Testing

### Quick connection test
```bash
python scripts/quick_test.py
```

---

## 🔍 Search

### Search by keyword
```bash
python scripts/search_keyword.py Governor
python scripts/search_keyword.py "flash loan"
python scripts/search_keyword.py reentrancy
python scripts/search_keyword.py oracle
```

### Interactive search
```bash
python scripts/interactive_search.py
```
Enter keywords and get results. To exit: `exit`, `quit` or `q`

---

## 📚 Examples

### Basic examples
```bash
python examples/basic_usage.py
```
Includes:
- Basic search
- Critical vulnerabilities search
- Keyword search

### Advanced examples
```bash
python examples/advanced_usage.py
```
Includes:
- Search by firms
- Search by tags
- Recent findings
- Advanced filters

---

## 💻 Use in code

```python
from src.solodit_client import SoloditClient

# Create client
client = SoloditClient()

# Search
data = client.search_findings(
    page=1,
    page_size=10,
    filters={"keywords": "reentrancy"}
)

# Print results
for finding in data['findings']:
    print(f"[{finding['impact']}] {finding['title']}")
```

---

## 📊 Popular queries

```bash
# Vulnerabilities in Governor contracts
python scripts/search_keyword.py Governor

# Reentrancy attacks
python scripts/search_keyword.py reentrancy

# Oracle issues
python scripts/search_keyword.py oracle

# Flash loan attacks
python scripts/search_keyword.py "flash loan"

# Access control issues
python scripts/search_keyword.py "access control"

# Price manipulation
python scripts/search_keyword.py "price manipulation"
```

---

## 🛑 Deactivate environment

When finished:
```bash
deactivate
```

---

## 📖 Full documentation

- **[SETUP.md](docs/SETUP.md)** - Installation and setup
- **[USAGE.md](docs/USAGE.md)** - Detailed guide
- **[API_SPECIFICATION.md](docs/API_SPECIFICATION.md)** - API specification

---

## ⚡ Command structure

| Command | Description |
|---------|-------------|
| `source venv/bin/activate` | Activate venv (Linux/Mac) |
| `venv\Scripts\activate` | Activate venv (Windows) |
| `python scripts/quick_test.py` | Connection test |
| `python scripts/search_keyword.py <word>` | Search by word |
| `python scripts/interactive_search.py` | Interactive mode |
| `python examples/basic_usage.py` | Basic examples |
| `python examples/advanced_usage.py` | Advanced examples |
| `deactivate` | Deactivate venv |

---

## 🎯 Example results

### Search "Governor" (350 findings)
- HIGH: 44
- MEDIUM: 111
- LOW: 171
- GAS: 24

### Search "reentrancy" (477 findings)
- HIGH: 189
- MEDIUM: 188
- LOW: 95
- GAS: 5

---

## 💡 Tips

1. **Rate limit**: 20 requests per minute
2. **Max results**: 100 per page
3. **Quality**: Filter by `qualityScore` (0-5)
4. **Rarity**: Filter by `rarityScore` (0-5)

---

## ❓ Problems?

See "Possible problems" section in [SETUP.md](docs/SETUP.md)
