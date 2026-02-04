# Saving All Findings to Single Markdown File

## Overview

The `save_findings_single_md.py` script saves all findings into **ONE** markdown file with table of contents, statistics, and full descriptions.

Perfect for:
- Creating reports
- Offline reading
- Converting to PDF
- Sharing with team

---

## Quick Start

### Basic usage

```bash
python scripts/save_findings_single_md.py supportsInterface 10 HIGH
```

This creates a single file: `findings_supportsInterface_20260127_181959.md`

---

## Usage

### Search by keyword

```bash
python scripts/save_findings_single_md.py reentrancy
```

### Specify count

```bash
python scripts/save_findings_single_md.py reentrancy 20
```

### Filter by impact

```bash
python scripts/save_findings_single_md.py oracle 15 HIGH
```

### Custom output filename

```bash
python scripts/save_findings_single_md.py Governor 10 HIGH my_report.md
```

### Multi-word keywords

```bash
python scripts/save_findings_single_md.py "flash loan" 10
```

---

## Command Syntax

```bash
python scripts/save_findings_single_md.py [keyword] [count] [impact] [output_file]
```

**Arguments:**
- `keyword` - Search keyword (optional)
- `count` - Number of findings (default: 10, max: 100)
- `impact` - Filter: HIGH, MEDIUM, LOW, GAS (optional)
- `output_file` - Custom filename (optional)

---

## Output Structure

The generated file contains:

### 1. Report Header
- Search query
- Total found
- Number included
- Generation timestamp

### 2. Statistics
- Average quality score
- Count by impact level
- Percentages

### 3. Table of Contents
- Clickable links to each finding
- Impact level indicators

### 4. Findings
Each finding includes:
- Quick info table (impact, quality, firm, protocol)
- Links (source, GitHub, PDF)
- Tags
- Found by (auditors)
- Full description (markdown)
- Summary

### 5. Footer
- Total count
- Timestamp

---

## Example Output

```markdown
# Security Findings Report

## Report Information
**Search Query:** `supportsInterface`
**Total Found:** 19 findings
**Included:** 5 findings
**Generated:** 2026-01-27 18:19:59

## Statistics
**Average Quality Score:** 2.00/5
**By Impact Level:**
- **HIGH:** 5 (100.0%)

## Table of Contents
1. [HIGH] [Token-gated airdrops don't work](#finding-1)
2. [HIGH] [NFT tokens may support both standards](#finding-2)
...

## Finding #1: Token-gated airdrops don't work {#finding-1}

### 📋 Quick Info
| Property | Value |
|----------|-------|
| **Impact** | HIGH |
| **Quality** | 5/5 ⭐ |
| **Firm** | Cyfrin |

### 📝 Description
[Full description here...]

---

## Finding #2: ...
```

---

## Use Cases

### 1. Create Security Report

```bash
python scripts/save_findings_single_md.py reentrancy 50 HIGH reentrancy_report.md
```

### 2. Research Specific Vulnerability

```bash
python scripts/save_findings_single_md.py "access control" 30
```

### 3. Study High-Quality Findings

```bash
# Search for quality >= 4 in code, then save
python scripts/save_findings_single_md.py oracle 20 HIGH
```

### 4. Create PDF Report

```bash
# Save to markdown
python scripts/save_findings_single_md.py Governor 15 HIGH

# Convert to PDF using pandoc
pandoc findings_Governor_*.md -o report.pdf
```

---

## Comparison: Single File vs Multiple Files

### Single File (`save_findings_single_md.py`)
✅ One file - easy to share
✅ Table of contents with links
✅ Statistics included
✅ Easy to convert to PDF
✅ Better for reports
❌ Large file size

### Multiple Files (`save_findings_to_md.py`)
✅ Separate files - easy to organize
✅ Smaller individual files
✅ Better for archiving
✅ Easy to search through
❌ Need to open multiple files
❌ No unified view

---

## Tips

### 1. Convert to PDF

```bash
# Using pandoc
pandoc findings_*.md -o report.pdf

# With custom styling
pandoc findings_*.md -o report.pdf --pdf-engine=xelatex
```

### 2. Open in Markdown Viewer

```bash
# VS Code
code findings_*.md

# Typora, Obsidian, or any markdown editor
```

### 3. Search Within File

```bash
# Search for specific text
grep -n "specific text" findings_*.md
```

### 4. Extract Statistics

```bash
# Count findings by impact
grep "^\*\*Impact\*\*" findings_*.md | sort | uniq -c
```

### 5. Share with Team

```bash
# Upload to GitHub
git add findings_*.md
git commit -m "Add security findings report"
git push

# Or share via email, Slack, etc.
```

---

## Examples

### Example 1: supportsInterface findings

```bash
python scripts/save_findings_single_md.py supportsInterface 10 HIGH
```

**Output:** `findings_supportsInterface_20260127_181959.md` (173.6 KB)

### Example 2: Reentrancy report

```bash
python scripts/save_findings_single_md.py reentrancy 50 HIGH reentrancy_report.md
```

**Output:** `reentrancy_report.md`

### Example 3: All HIGH severity

```bash
python scripts/save_findings_single_md.py "" 100 HIGH all_high_severity.md
```

---

## Advanced Usage

### Custom Filtering in Code

Modify the script to add more filters:

```python
filters = {
    "keywords": keyword,
    "impact": ["HIGH"],
    "qualityScore": 4,  # Only high quality
    "firms": [{"value": "Cyfrin"}],  # Specific firm
    "sortField": "Quality",
    "sortDirection": "Desc"
}
```

### Batch Processing

```bash
# Create multiple reports
for keyword in reentrancy oracle "flash loan"; do
    python scripts/save_findings_single_md.py "$keyword" 20 HIGH
done
```

---

## Troubleshooting

### Issue: File too large

**Solution:** Reduce count or filter by impact:
```bash
python scripts/save_findings_single_md.py keyword 20 HIGH
```

### Issue: "Rate limit exceeded"

**Solution:** Wait 60 seconds between runs.

### Issue: Can't open file

**Solution:** File might be too large. Try:
- Open in VS Code
- Use command line: `less findings_*.md`
- Split into smaller files

---

## Integration

### With Pandoc (PDF)

```bash
# Basic PDF
pandoc findings_*.md -o report.pdf

# With table of contents
pandoc findings_*.md -o report.pdf --toc

# With custom template
pandoc findings_*.md -o report.pdf --template=custom.tex
```

### With GitHub

```bash
# Add to repository
git add findings_*.md
git commit -m "Add findings report"
git push

# View on GitHub - automatic markdown rendering
```

### With Documentation Sites

```bash
# Copy to docs folder
cp findings_*.md docs/security-findings.md

# Use in MkDocs, Docusaurus, etc.
```

---

## See Also

- [SAVING_FINDINGS.md](SAVING_FINDINGS.md) - Multiple files version
- [FINDING_FORMAT.md](FINDING_FORMAT.md) - Finding format details
- [USAGE.md](USAGE.md) - General usage guide

---

## Help

```bash
python scripts/save_findings_single_md.py --help
```

Shows usage information and examples.
