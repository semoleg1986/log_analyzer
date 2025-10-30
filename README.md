# CLI log analyzer

CLI-утилита для анализа лог-файлов.

---

## Запуск с аргументами
```bash
python main.py --file test.log --keywords "INFO, ERROR"
```
	•	--file FILE - Путь к файлу с логами
	•	--keywords KEYWORDS - Список ключевых слов через запятую, например: ERROR,WARNING

## Пример вывода

| FILENAME   | INFO    | ERROR | LINES    |
|------------|---------|-------|----------|
| test.log   | 4       | 3     | 9        |


## Тесты
Запуск тестов через pytest:
```commandline
make test
```

## Makefile
```bash
make run    # запуск приложения
make test   # запуск тестов
make lint   # проверка типизации через mypy
```

## Технологии
	•	Python 3.11+
	•	pytest
    •	tabulate
	•	mypy

## Структура проекта.
```commandline
cli_calculator/
├── Makefile
├── README.md
├── __init__.py
├── analyzer.py            # Анализатор логов
├── cli.py                 # CLI-интерфейс (App)
├── main.py                # Точка входа
├── args.py                # Парсит аргументы командной строки
├── utils/
│   ├── __init__.py
│   └── logger.py          # Настройка логирования
└── tests/
    ├── __init__.py
    └── test_cli.py  # Юнит-тесты
```
