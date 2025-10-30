import argparse

LOGS_DEFAULT = "ERROR,WARNING"


def parse_args() -> argparse.Namespace:
    """
    Парсит аргументы командной строки.

    :return: Объект Namespace с путём к файлу.
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description="CLI log analyzer")
    parser.add_argument("--file", required=True, help="Путь к файлу с логами")
    parser.add_argument(
        "--keywords",
        type=str,
        default=LOGS_DEFAULT,
        help="Список ключевых слов через запятую, например: ERROR,WARNING",
    )
    return parser.parse_args()
