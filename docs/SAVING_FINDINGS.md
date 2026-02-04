# Saving Findings to Markdown Files

## Overview

The `save_findings_to_md.py` script allows you to search for findings and save them as individual markdown files for easy reading and archiving.

## Usage

### Basic usage

```bash
python scripts/save_findings_to_md.py
```

This will save 10 random findings to a timestamped directory.

### Search by keyword

```bash
python scripts/save_findings_to_md.py reentrancy
```

Saves 10 findings related to "reentrancy".

### Specify count

```bash
python scripts/save_findings_to_md.py reentrancy 20
```

Saves 20 findings related to "reentrancy".

### Filter by impact

```bash
python scripts/save_findings_to_md.py oracle 15 HIGH
```

Saves 15 HIGH severity findings related to "oracle".

### Multi-word keywords

```bash
python scripts/save_findings_to_md.py "flash loan" 10
```

Use quotes for multi-word keywords.

---

## Command syntax

```bash
python scripts/save_findings_to_md.py [keyword] [count] [impact]
```

**Arguments:**
- `keyword` - Search keyword (optional)
- `count` - Number of findings to save (default: 10, max: 100)
- `impact` - Filter by impact: HIGH, MEDIUM, LOW, GAS (optional)

---

## Examples

### Example 1: Save reentrancy findings

```bash
python scripts/save_findings_to_md.py reentrancy 5 HIGH
```

**Output:**
```
================================================================================
SAVE FINDINGS TO MARKDOWN FILES
================================================================================

🔍 Searching for: 'reentrancy'
📊 Impact filter: HIGH
📄 Requesting 5 findings...

✅ Found 226 total findings
📥 Saving 5 findings to markdown files...

 1. [HIGH] Read-only reentrancy... → findings_reentrancy_20260127_181046/01_...
 2. [HIGH] Reentrancy in withdraw... → findings_reentrancy_20260127_181046/02_...
 ...

================================================================================
✅ Successfully saved 5 findings!
📁 Output directory: findings_reentrancy_20260127_181046/
📋 Index file: findings_reentrancy_20260127_181046/INDEX.md
================================================================================
```

### Example 2: Save oracle issues

```bash
python scripts/save_findings_to_md.py oracle 10
```

### Example 3: Save all HIGH severity findings

```bash
python scripts/save_findings_to_md.py "" 20 HIGH
```

### Example 4: Save Governor findings

```bash
python scripts/save_findings_to_md.py Governor 15
```

---

## Output structure

### Directory structure

```
findings_reentrancy_20260127_181046/
├── INDEX.md                    # Index with all findings
├── 01_Finding_Title.md         # First finding
├── 02_Finding_Title.md         # Second finding
├── 03_Finding_Title.md         # Third finding
└── ...
```

### INDEX.md

The index file contains:
- Search parameters
- Statistics (count by impact level)
- List of all findings with links

**Example:**
```markdown
# Findings Index

**Search keyword:** `reentrancy`
**Total found:** 226 findings
**Saved:** 5 findings
**Generated:** 2026-01-27 18:10:46

## Statistics
- **HIGH:** 5

## Findings
### 1. [HIGH] Read-only reentrancy
- **Quality:** 5/5
- **Firm:** Cyfrin
- **File:** [01_Read-only reentrancy.md](01_Read-only reentrancy.md)
...
```

### Individual finding file

Each finding file contains:

1. **Title** - Finding title
2. **Metadata** - Impact, quality, firm, protocol, links
3. **Tags** - Vulnerability tags
4. **Found By** - List of auditors
5. **Description** - Full vulnerability description (markdown)
6. **Summary** - AI-generated summary (if available)

**Example structure:**
```markdown
# Read-only reentrancy
---
## Metadata
- **Impact:** HIGH
- **Quality Score:** 5/5
- **Rarity Score:** 5/5
- **Audit Firm:** Cyfrin
- **Protocol:** Beanstalk Wells
- **Source:** [link](url)

## Tags
`Read-only Reentrancy`

## Found By
- Hans
- Alex Roan
- Patrick Collins

---

## Description

[Full vulnerability description in markdown format]

---

## Summary

[AI-generated summary]
```

---

## Use cases

### 1. Research specific vulnerability type

```bash
python scripts/save_findings_to_md.py "access control" 50 HIGH
```

Save 50 HIGH severity access control findings for research.

### 2. Create vulnerability database

```bash
# Save different types
python scripts/save_findings_to_md.py reentrancy 100
python scripts/save_findings_to_md.py oracle 100
python scripts/save_findings_to_md.py "flash loan" 100
```

### 3. Study high-quality findings

```bash
# Search in code for quality >= 4
from src.solodit_client import SoloditClient

client = SoloditClient()
data = client.search_findings(
    page=1,
    page_size=50,
    filters={
        "qualityScore": 4,
        "impact": ["HIGH"]
    }
)
```

Then save manually or modify the script.

### 4. Archive findings by firm

```bash
# Modify script to filter by firm
python scripts/save_findings_to_md.py "" 100
# Then filter by firm in code
```

---

## Tips

### 1. Organize by topic

Create separate directories for different topics:
```bash
python scripts/save_findings_to_md.py reentrancy 50
python scripts/save_findings_to_md.py oracle 50
python scripts/save_findings_to_md.py "integer overflow" 50
```

### 2. Filter high-quality findings

Use HIGH impact and check quality scores in INDEX.md:
```bash
python scripts/save_findings_to_md.py reentrancy 100 HIGH
# Then review INDEX.md and focus on quality >= 4
```

### 3. Read offline

Save findings and read them offline:
```bash
python scripts/save_findings_to_md.py "your topic" 50
# Copy findings_* directory to another device
```

### 4. Convert to PDF

Use markdown to PDF converters:
```bash
# Using pandoc
pandoc findings_*/01_*.md -o finding.pdf

# Or use online converters
```

### 5. Search within saved findings

```bash
# Search for specific text in all saved findings
grep -r "specific text" findings_*/
```

---

## Limitations

- **Max count:** 100 findings per run (API limitation)
- **Rate limit:** 20 requests per minute
- **Filename length:** Titles are truncated to 100 characters
- **Special characters:** Unsafe characters in filenames are replaced with `_`

---

## Troubleshooting

### Issue: "Rate limit exceeded"

**Solution:** Wait 60 seconds before running again.

### Issue: "No findings found"

**Solution:** Try different keywords or remove impact filter.

### Issue: "Filename too long"

**Solution:** This is handled automatically - titles are truncated.

### Issue: "Permission denied"

**Solution:** Make sure you have write permissions in the current directory.

---

## Advanced usage

### Modify the script

You can modify `scripts/save_findings_to_md.py` to:

1. **Add more filters:**
```python
filters = {
    "keywords": keyword,
    "impact": ["HIGH"],
    "qualityScore": 4,  # Add quality filter
    "firms": [{"value": "Cyfrin"}]  # Add firm filter
}
```

2. **Change output format:**
```python
# Modify save_finding_to_md() function
# Add custom sections or formatting
```

3. **Save to different formats:**
```python
# Add JSON export
import json
with open('finding.json', 'w') as f:
    json.dump(finding, f, indent=2)
```

---

## Integration with other tools

### 1. Create a database

```python
import sqlite3

# Create database from saved findings
conn = sqlite3.connect('findings.db')
# Insert findings data
```

### 2. Generate reports

```python
# Use saved findings to generate reports
# Analyze trends, statistics, etc.
```

### 3. Build search index

```python
# Use Elasticsearch or similar
# Index all saved findings for fast search
```

---

## See also

- [USAGE.md](USAGE.md) - General usage guide
- [FINDING_FORMAT.md](FINDING_FORMAT.md) - Finding format details
- [API_SPECIFICATION.md](API_SPECIFICATION.md) - Full API documentation

---

## Help

```bash
python scripts/save_findings_to_md.py --help
```

Shows usage information and examples.
