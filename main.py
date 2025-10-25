#!/usr/bin python3
import sys
from pathlib import Path

from args import parse_args
from cli import App


def main():
    """
    Точка входа в программу CLI Log Analyzer.

    - Считывает лог-файл (например, app.log).
    - Подсчитывает:
        1. количество строк с ERROR;
        2. количество строк с WARNING;
        3. общее число строк.
    - Выводит сводку в табличном формате (tabulate).
    """
    args = parse_args()
    file_path = Path(args.file)

    if not file_path.exists():
        print(f"Ошибка: файл '{file_path}' не найден.")
        sys.exit(1)

    if file_path.stat().st_size == 0:
        print(f"Файл '{file_path}' пуст.")
        sys.exit(1)

    app = App(args=args)
    app.run()


if __name__ == "__main__":
    main()
