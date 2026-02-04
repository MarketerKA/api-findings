# Руководство по использованию

## Быстрый старт

### 1. Активация окружения

```bash
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

### 2. Быстрый тест

```bash
python scripts/quick_test.py
```

## Скрипты

### Поиск по ключевому слову

```bash
python scripts/search_keyword.py Governor
python scripts/search_keyword.py "flash loan"
python scripts/search_keyword.py reentrancy
```

Вывод:
- Общее количество найденных findings
- Первые 10 результатов
- Статистика по уровням серьезности (HIGH, MEDIUM, LOW, GAS)

### Интерактивный поиск

```bash
python scripts/interactive_search.py
```

Интерактивный режим позволяет вводить ключевые слова и сразу видеть результаты.

Для выхода введите: `exit`, `quit` или `q`

## Примеры использования

### Базовые примеры

```bash
python examples/basic_usage.py
```

Включает:
- Базовый поиск
- Поиск критических уязвимостей (HIGH)
- Поиск по ключевым словам

### Продвинутые примеры

```bash
python examples/advanced_usage.py
```

Включает:
- Поиск по аудиторским фирмам
- Поиск по тегам
- Недавние findings
- Продвинутые фильтры

## Использование в коде

### Базовый пример

```python
from src.solodit_client import SoloditClient

# Создание клиента
client = SoloditClient()

# Поиск findings
data = client.search_findings(page=1, page_size=10)

# Вывод результатов
for finding in data['findings']:
    print(f"[{finding['impact']}] {finding['title']}")
```

### Поиск по ключевому слову

```python
data = client.search_findings(
    page=1,
    page_size=50,
    filters={"keywords": "reentrancy"}
)
```

### Поиск критических уязвимостей

```python
data = client.get_high_severity_findings(page=1, page_size=20)
```

### Поиск по фирмам

```python
data = client.search_by_firm(
    firms=["Cyfrin", "Sherlock"],
    page=1,
    page_size=25
)
```

### Поиск по тегам

```python
data = client.search_by_tags(
    tags=["Oracle", "Reentrancy"],
    impact=["HIGH"],
    page=1,
    page_size=30
)
```

### Недавние findings

```python
# Последние 30 дней
data = client.get_recent_findings(days=30, page=1, page_size=50)

# Последние 60 дней
data = client.get_recent_findings(days=60, page=1, page_size=50)

# Последние 90 дней
data = client.get_recent_findings(days=90, page=1, page_size=50)
```

### Продвинутые фильтры

```python
data = client.search_findings(
    page=1,
    page_size=50,
    filters={
        "keywords": "oracle",
        "impact": ["HIGH", "MEDIUM"],
        "qualityScore": 3,  # Минимальное качество 3/5
        "rarityScore": 2,   # Минимальная редкость 2/5
        "languages": [{"value": "Solidity"}],
        "firms": [{"value": "Cyfrin"}],
        "tags": [{"value": "Oracle"}],
        "sortField": "Quality",
        "sortDirection": "Desc"
    }
)
```

## Структура ответа

```python
{
    "findings": [
        {
            "id": "...",
            "title": "...",
            "impact": "HIGH",  # HIGH, MEDIUM, LOW, GAS
            "quality_score": 4,  # 0-5
            "general_score": 3,  # 0-5 (rarity)
            "firm_name": "Cyfrin",
            "protocol_name": "...",
            "content": "...",  # Полное описание
            "source_link": "...",
            # ... другие поля
        }
    ],
    "metadata": {
        "totalResults": 350,
        "currentPage": 1,
        "pageSize": 50,
        "totalPages": 7,
        "elapsed": 0.123
    },
    "rateLimit": {
        "limit": 20,
        "remaining": 19,
        "reset": 1234567890
    }
}
```

## Доступные фильтры

### Уровни серьезности (impact)
- `HIGH` - Критические уязвимости
- `MEDIUM` - Средние уязвимости
- `LOW` - Низкие уязвимости
- `GAS` - Оптимизация газа

### Популярные фирмы (firms)
- Cyfrin
- Sherlock
- Code4rena
- Trail of Bits
- OpenZeppelin
- Consensys Diligence
- Spearbit
- И другие...

### Популярные теги (tags)
- Reentrancy
- Oracle
- Access Control
- Integer Overflow/Underflow
- Front-running
- Logic Error
- DOS
- Price Manipulation
- Flash Loan
- И другие...

### Языки программирования (languages)
- Solidity
- Rust
- Cairo
- Vyper
- Move

### Сортировка (sortField)
- `Recency` - По дате (по умолчанию)
- `Quality` - По качеству
- `Rarity` - По редкости

### Направление сортировки (sortDirection)
- `Desc` - По убыванию (по умолчанию)
- `Asc` - По возрастанию

## Rate Limiting

- Лимит: 20 запросов в 60 секунд
- Информация о лимите возвращается в каждом ответе
- При превышении лимита API вернет ошибку 429

Пример проверки rate limit:

```python
data = client.search_findings(page=1, page_size=10)
rate_limit = data['rateLimit']

print(f"Осталось запросов: {rate_limit['remaining']}/{rate_limit['limit']}")
```

## Пагинация

```python
# Получить все результаты (с учетом rate limit)
all_findings = []
page = 1

while True:
    data = client.search_findings(
        page=page,
        page_size=100,  # Максимум 100
        filters={"keywords": "reentrancy"}
    )
    
    all_findings.extend(data['findings'])
    
    if page >= data['metadata']['totalPages']:
        break
    
    page += 1
    
    # Пауза для соблюдения rate limit
    import time
    time.sleep(3)

print(f"Всего получено: {len(all_findings)} findings")
```
