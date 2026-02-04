# Solodit API Client

Python client for working with Cyfrin Solodit Findings API - search and analyze vulnerabilities from smart contract security audits.

## 👋 New here? Start here!

**➡️ [START_HERE.md](START_HERE.md)** - Quick start in 3 steps!

## 📁 Project Structure

```
Soldit-api/
├── src/                      # Source code
│   ├── __init__.py
│   └── solodit_client.py    # Main API client
├── scripts/                  # Ready-to-use scripts
│   ├── quick_test.py        # Quick connection test
│   ├── search_keyword.py    # Search by keyword
│   ├── interactive_search.py # Interactive search
│   ├── show_finding_format.py # Show finding format
│   └── simple_finding_example.py # Simple example
├── examples/                 # Usage examples
│   ├── basic_usage.py       # Basic examples
│   └── advanced_usage.py    # Advanced examples
├── docs/                     # Documentation
│   ├── SETUP.md             # Installation and setup
│   ├── USAGE.md             # Usage guide
│   ├── FINDING_FORMAT.md    # Finding format guide
│   └── API_SPECIFICATION.md # Full API specification
├── venv/                     # Virtual environment
├── .env                      # API key
├── .gitignore
├── requirements.txt          # Dependencies
└── README.md                 # This file
```

## 🚀 Quick Start

### 1. Activate virtual environment

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 2. Quick test

```bash
python scripts/quick_test.py
```

### 3. Search by keyword

```bash
python scripts/search_keyword.py Governor
```

### 4. Interactive search

```bash
python scripts/interactive_search.py
```

## 📚 Documentation

- **[START_HERE.md](START_HERE.md)** - 👋 Quick start in 3 steps (start here!)
- **[QUICKSTART.md](QUICKSTART.md)** - 🚀 All commands and examples
- **[INDEX.md](INDEX.md)** - 📑 Navigation through all files
- **[FILES_OVERVIEW.md](FILES_OVERVIEW.md)** - 📋 Overview of all project files
- **[SETUP.md](docs/SETUP.md)** - 🔧 Detailed installation and setup instructions
- **[USAGE.md](docs/USAGE.md)** - 📖 Usage guide with examples
- **[FINDING_FORMAT.md](docs/FINDING_FORMAT.md)** - 📄 Finding format and data structure
- **[SAVING_FINDINGS.md](docs/SAVING_FINDINGS.md)** - 💾 How to save findings to MD files
- **[API_SPECIFICATION.md](docs/API_SPECIFICATION.md)** - 📋 Full API specification
- **[PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md)** - 📁 Project structure

## 💡 Usage Examples

### Basic search

```python
from src.solodit_client import SoloditClient

client = SoloditClient()
data = client.search_findings(page=1, page_size=10)

for finding in data['findings']:
    print(f"[{finding['impact']}] {finding['title']}")
```

### Search by keyword

```python
data = client.search_findings(
    page=1,
    page_size=50,
    filters={"keywords": "reentrancy"}
)
```

### Critical vulnerabilities

```python
data = client.get_high_severity_findings(page=1, page_size=20)
```

### Search by firms

```python
data = client.search_by_firm(
    firms=["Cyfrin", "Sherlock"],
    page=1,
    page_size=25
)
```

More examples in [USAGE.md](docs/USAGE.md)

## 🛠️ Available Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `quick_test.py` | Quick connection test | `python scripts/quick_test.py` |
| `search_keyword.py` | Search by keyword | `python scripts/search_keyword.py <keyword>` |
| `interactive_search.py` | Interactive search mode | `python scripts/interactive_search.py` |
| `show_finding_format.py` | Show complete finding format | `python scripts/show_finding_format.py` |
| `simple_finding_example.py` | Simple finding example | `python scripts/simple_finding_example.py` |
| `save_findings_to_md.py` | Save findings to MD files | `python scripts/save_findings_to_md.py <keyword> <count>` |
| `save_findings_single_md.py` | Save all findings to ONE MD file | `python scripts/save_findings_single_md.py <keyword> <count>` |

## 📦 Examples

| File | Description | Usage |
|------|-------------|-------|
| `basic_usage.py` | Basic examples | `python examples/basic_usage.py` |
| `advanced_usage.py` | Advanced examples | `python examples/advanced_usage.py` |

## 🔑 API Features

- ✅ Search findings with filters
- ✅ Filter by severity level (HIGH, MEDIUM, LOW, GAS)
- ✅ Search by keywords
- ✅ Filter by audit firms
- ✅ Filter by vulnerability tags
- ✅ Filter by protocols and categories
- ✅ Filter by programming languages
- ✅ Sort by quality, rarity, date
- ✅ Pagination (up to 100 results per page)
- ✅ Rate limiting: 20 requests per minute

## 📊 Example Result

```
🔍 Searching for keyword: 'Governor'
============================================================

✅ Total found: 350 findings

📊 Statistics by severity level:
------------------------------------------------------------
HIGH     :    44 findings
MEDIUM   :   111 findings
LOW      :   171 findings
GAS      :    24 findings
```

## 🔧 Requirements

- Python 3.8+
- requests
- python-dotenv

## 📝 Installation

Detailed instructions in [SETUP.md](docs/SETUP.md)

```bash
# Activate venv
source venv/bin/activate

# Install dependencies (already installed)
pip install -r requirements.txt
```

## 🔐 API Key

API key is already configured in `.env`. To get a new key:

1. Create an account on [solodit.cyfrin.io](https://solodit.cyfrin.io)
2. Open menu → API Keys
3. Generate new key

## 📞 Support

- Email: support@cyfrin.io
- Website: https://solodit.cyfrin.io

## 📄 License

This project is created for working with Cyfrin Solodit API.
