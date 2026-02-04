# Finding Format Documentation

## Overview

When you search for findings using the Solodit API, you receive a JSON response containing an array of finding objects. Each finding represents a security vulnerability discovered during a smart contract audit.

## Response Structure

```python
{
    "findings": [
        { ... finding object ... },
        { ... finding object ... },
        ...
    ],
    "metadata": {
        "totalResults": 8022,
        "currentPage": 1,
        "pageSize": 50,
        "totalPages": 161,
        "elapsed": 0.234
    },
    "rateLimit": {
        "limit": 20,
        "remaining": 19,
        "reset": 1234567890
    }
}
```

## Finding Object Structure

### Basic Information

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `id` | string | Unique finding ID | "64110" |
| `title` | string | Finding title | "[H-01] Reentrancy vulnerability" |
| `impact` | string | Severity level | "HIGH", "MEDIUM", "LOW", "GAS" |
| `quality_score` | number | Quality rating (0-5) | 4.5 |
| `general_score` | number | Rarity score (0-5) | 3.5 |
| `kind` | string | Content format | "MARKDOWN", "GIT" |

### Content

| Field | Type | Description |
|-------|------|-------------|
| `content` | string | Full vulnerability description (Markdown) |
| `summary` | string | AI-generated summary |

**Example:**
```python
finding = data['findings'][0]
content = finding['content']  # Full markdown text
summary = finding['summary']  # Short summary
```

### Audit Firm

| Field | Type | Description |
|-------|------|-------------|
| `firm_name` | string | Audit firm name |
| `auditfirm_id` | string | Firm ID |
| `firm_logo_square` | string | Logo filename |

**Example:**
```python
firm = finding.get('firm_name')  # "Cyfrin"
logo = finding.get('firm_logo_square')  # "Cyfrin_square.png"
```

### Protocol

| Field | Type | Description |
|-------|------|-------------|
| `protocol_name` | string | Protocol name |
| `protocol_id` | string | Protocol ID |
| `protocols_protocol` | object | Protocol details |

**Example:**
```python
protocol = finding.get('protocol_name')  # "Uniswap V3"
```

### Links

| Field | Type | Description |
|-------|------|-------------|
| `source_link` | string | Link to original report |
| `github_link` | string | GitHub link (if available) |
| `pdf_link` | string | PDF link (if available) |
| `pdf_page_from` | number | Starting page in PDF |

**Example:**
```python
link = finding.get('source_link')
has_pdf = finding.get('pdf_link') is not None
```

### Dates

| Field | Type | Description |
|-------|------|-------------|
| `report_date` | string/object | Report publication date |

### Finders (Auditors)

| Field | Type | Description |
|-------|------|-------------|
| `finders_count` | number | Number of finders |
| `issues_issue_finders` | array | List of finders |

**Structure:**
```python
{
    "finders_count": 2,
    "issues_issue_finders": [
        {
            "wardens_warden": {
                "handle": "auditor1"
            }
        },
        {
            "wardens_warden": {
                "handle": "auditor2"
            }
        }
    ]
}
```

**Example:**
```python
# Get all finder handles
finders = [
    f['wardens_warden']['handle'] 
    for f in finding.get('issues_issue_finders', [])
]
# Result: ['auditor1', 'auditor2']
```

### Tags

| Field | Type | Description |
|-------|------|-------------|
| `issues_issuetagscore` | array | List of vulnerability tags |

**Structure:**
```python
{
    "issues_issuetagscore": [
        {
            "tags_tag": {
                "title": "Reentrancy"
            }
        },
        {
            "tags_tag": {
                "title": "Access Control"
            }
        }
    ]
}
```

**Example:**
```python
# Get all tags
tags = [
    tag['tags_tag']['title'] 
    for tag in finding.get('issues_issuetagscore', [])
]
# Result: ['Reentrancy', 'Access Control']
```

### Contest Information (for competitive audits)

| Field | Type | Description |
|-------|------|-------------|
| `contest_id` | string | Contest ID |
| `contest_link` | string | Contest link |
| `contest_prize_txt` | string | Prize information |
| `sponsor_name` | string | Sponsor name |
| `sponsor_link` | string | Sponsor link |

### User-specific (always false for API)

| Field | Type | Description |
|-------|------|-------------|
| `bookmarked` | boolean | Always false |
| `read` | boolean | Always false |

## Common Usage Patterns

### 1. Get Basic Information

```python
finding = data['findings'][0]

title = finding['title']
impact = finding['impact']
quality = finding['quality_score']
firm = finding.get('firm_name')
protocol = finding.get('protocol_name')

print(f"[{impact}] {title}")
print(f"Firm: {firm}, Protocol: {protocol}")
print(f"Quality: {quality}/5")
```

### 2. Get Full Content

```python
# Content is in Markdown format
content = finding['content']

# Save to file
with open('vulnerability.md', 'w') as f:
    f.write(content)
```

### 3. Extract All Tags

```python
tags = [
    tag['tags_tag']['title'] 
    for tag in finding.get('issues_issuetagscore', [])
]

print(f"Tags: {', '.join(tags)}")
```

### 4. Extract All Finders

```python
finders = [
    f['wardens_warden']['handle'] 
    for f in finding.get('issues_issue_finders', [])
]

print(f"Found by: {', '.join(finders)}")
```

### 5. Check for Links

```python
has_source = finding.get('source_link') is not None
has_github = finding.get('github_link') is not None
has_pdf = finding.get('pdf_link') is not None

if has_source:
    print(f"Source: {finding['source_link']}")
```

### 6. Filter by Quality

```python
high_quality = [
    f for f in data['findings'] 
    if f['quality_score'] >= 4
]

print(f"High quality findings: {len(high_quality)}")
```

### 7. Group by Impact

```python
from collections import defaultdict

by_impact = defaultdict(list)
for finding in data['findings']:
    by_impact[finding['impact']].append(finding)

print(f"HIGH: {len(by_impact['HIGH'])}")
print(f"MEDIUM: {len(by_impact['MEDIUM'])}")
print(f"LOW: {len(by_impact['LOW'])}")
```

### 8. Create Summary Report

```python
for finding in data['findings']:
    print(f"\n{'='*80}")
    print(f"[{finding['impact']}] {finding['title']}")
    print(f"Firm: {finding.get('firm_name', 'N/A')}")
    print(f"Quality: {finding['quality_score']}/5")
    
    tags = [t['tags_tag']['title'] for t in finding.get('issues_issuetagscore', [])]
    if tags:
        print(f"Tags: {', '.join(tags)}")
    
    if finding.get('source_link'):
        print(f"Link: {finding['source_link']}")
```

### 9. Export to CSV

```python
import csv

with open('findings.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Impact', 'Quality', 'Firm', 'Protocol', 'Link'])
    
    for finding in data['findings']:
        writer.writerow([
            finding['title'],
            finding['impact'],
            finding['quality_score'],
            finding.get('firm_name', ''),
            finding.get('protocol_name', ''),
            finding.get('source_link', '')
        ])
```

### 10. Save Full Finding as JSON

```python
import json

finding = data['findings'][0]

with open('finding.json', 'w') as f:
    json.dump(finding, f, indent=2)
```

## Content Format

The `content` field contains the full vulnerability description in **Markdown format**. This typically includes:

- Severity assessment
- Detailed description
- Code snippets
- Proof of concept
- Recommendations
- Impact analysis

**Example content structure:**
```markdown
## Severity

**Impact:** High
**Likelihood:** Medium

## Description

The contract contains a reentrancy vulnerability...

## Proof of Concept

```solidity
function withdraw() public {
    // Vulnerable code
}
```

## Recommendations

Use the checks-effects-interactions pattern...
```

## Testing Scripts

We provide several scripts to explore finding formats:

### 1. Show Complete Format
```bash
python scripts/show_finding_format.py
```
Shows the complete JSON structure and all available fields.

### 2. Simple Example
```bash
python scripts/simple_finding_example.py
```
Shows a simplified view with the most important fields.

### 3. Search and Display
```bash
python scripts/search_keyword.py reentrancy
```
Search for findings and display key information.

## Tips

1. **Always use `.get()`** for optional fields to avoid KeyError
2. **Content is Markdown** - you can render it or save as .md files
3. **Tags and finders are nested** - use list comprehensions to extract
4. **Check for None/empty** values before using links
5. **Quality and rarity scores** help filter high-value findings
6. **Impact levels** are: HIGH, MEDIUM, LOW, GAS

## Example: Complete Finding Processing

```python
from src.solodit_client import SoloditClient

client = SoloditClient()

# Search for high-quality reentrancy findings
data = client.search_findings(
    page=1,
    page_size=10,
    filters={
        "keywords": "reentrancy",
        "impact": ["HIGH"],
        "qualityScore": 4
    }
)

# Process each finding
for finding in data['findings']:
    # Basic info
    title = finding['title']
    impact = finding['impact']
    quality = finding['quality_score']
    
    # Source
    firm = finding.get('firm_name', 'Unknown')
    protocol = finding.get('protocol_name', 'Unknown')
    
    # Content
    content = finding.get('content', '')
    
    # Tags
    tags = [t['tags_tag']['title'] for t in finding.get('issues_issuetagscore', [])]
    
    # Finders
    finders = [f['wardens_warden']['handle'] for f in finding.get('issues_issue_finders', [])]
    
    # Links
    source_link = finding.get('source_link')
    
    # Print summary
    print(f"\n[{impact}] {title}")
    print(f"Firm: {firm} | Protocol: {protocol}")
    print(f"Quality: {quality}/5")
    if tags:
        print(f"Tags: {', '.join(tags)}")
    if finders:
        print(f"Found by: {', '.join(finders)}")
    if source_link:
        print(f"Link: {source_link}")
    
    # Save content
    filename = f"finding_{finding['id']}.md"
    with open(filename, 'w') as f:
        f.write(f"# {title}\n\n")
        f.write(f"**Impact:** {impact}\n")
        f.write(f"**Quality:** {quality}/5\n")
        f.write(f"**Firm:** {firm}\n")
        f.write(f"**Protocol:** {protocol}\n\n")
        f.write(content)
    
    print(f"Saved to: {filename}")
```

## See Also

- [API Specification](API_SPECIFICATION.md) - Full API documentation
- [Usage Guide](USAGE.md) - How to use the client
- Run `python scripts/show_finding_format.py` for live examples
