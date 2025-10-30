#!/usr/bin python3
import sys
from pathlib import Path

from cli import App
from utils.args import parse_args
from utils.logger import get_logger

logger = get_logger(__name__)


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
        msg = f"Ошибка: файл '{file_path}' не найден."
        print(msg)
        logger.error(msg)
        sys.exit(1)

    if file_path.stat().st_size == 0:
        msg = f"Файл '{file_path}' пуст."
        print(msg)
        logger.warning(msg)
        sys.exit(1)

    app = App(args=args)
    app.run()


if __name__ == "__main__":
    main()
