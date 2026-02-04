---
inclusion: always
---

# Project Rules for Solodit API Client

## File Creation Rules

### ❌ DO NOT CREATE:

1. **Markdown files** unless explicitly requested by the user
   - No summary files
   - No documentation files
   - No report files
   - Exception: Only when user specifically asks for MD file

2. **Test/Example output files** without permission
   - No `findings_*.md` files
   - No `test_*.md` files
   - No `report_*.md` files

3. **Unnecessary documentation**
   - Don't create new docs unless requested
   - Don't duplicate existing documentation

### ✅ ALLOWED:

1. **Code files** (.py) when implementing features
2. **Configuration files** when needed (.env.example, .gitignore)
3. **Documentation updates** when fixing or improving existing docs
4. **Output files** only when user runs export scripts themselves

## Code Style

- All code and comments in **English**
- Clean, minimal implementations
- No verbose code
- Follow existing project structure

## Documentation

- Keep documentation concise
- Update existing docs instead of creating new ones
- All documentation in **English**

## User Requests

- Only create files that user explicitly requests
- Ask for confirmation before creating multiple files
- Clean up test files after demonstrations
