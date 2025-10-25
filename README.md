# CLI log analyzer

CLI-утилита для анализа лог-файлов.

---
## Запуск
Интерактивный режим 
```bash
python main.py
```

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
