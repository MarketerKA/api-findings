# Установка и настройка

## Требования

- Python 3.8 или выше
- pip (менеджер пакетов Python)

## Установка

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd Soldit-api
```

### 2. Создание виртуального окружения

**Linux/Mac:**
```bash
python3 -m venv venv
```

**Windows:**
```bash
python -m venv venv
```

### 3. Активация виртуального окружения

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows (CMD):**
```bash
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

После активации в начале строки терминала появится `(venv)`.

### 4. Установка зависимостей

```bash
pip install -r requirements.txt
```

## Настройка API ключа

API ключ уже настроен в файле `.env`:

```env
API_KEY=sk_4db18175ab3aa879002b2406e5d2e3264fc64cf5b2ff4b341d940ba48e5b4413
```

Если нужно использовать другой ключ:

1. Откройте файл `.env`
2. Замените значение `API_KEY` на ваш ключ
3. Сохраните файл

### Получение API ключа

1. Создайте аккаунт на [solodit.cyfrin.io](https://solodit.cyfrin.io)
2. Откройте выпадающее меню в правом верхнем углу
3. Откройте модальное окно "API Keys"
4. Сгенерируйте новый API ключ

## Проверка установки

Запустите быстрый тест:

```bash
python scripts/quick_test.py
```

Если все настроено правильно, вы увидите:
```
✅ Клиент создан успешно
✅ Подключение успешно!
✅ Все тесты пройдены успешно!
```

## Деактивация виртуального окружения

Когда закончите работу:

```bash
deactivate
```

## Возможные проблемы

### Ошибка: "API key не найден"

**Решение:** Убедитесь, что файл `.env` существует и содержит корректный API ключ.

### Ошибка: "Module not found"

**Решение:** Убедитесь, что виртуальное окружение активировано и зависимости установлены:
```bash
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install -r requirements.txt
```

### Ошибка: "Rate limit exceeded"

**Решение:** Подождите 60 секунд. Лимит: 20 запросов в минуту.

### Ошибка: "Invalid API key"

**Решение:** Проверьте правильность API ключа в файле `.env`.
