from pathlib import Path
from typing import TYPE_CHECKING

from tabulate import tabulate

from core.analyzer import LogAnalyzer
from utils.args import parse_args
from utils.logger import get_logger

logger = get_logger(__name__)

if TYPE_CHECKING:
    import argparse


class App:
    """
    CLI-приложение
    """

    def __init__(
        self, analyzer_cls=LogAnalyzer, args: "argparse.Namespace | None" = None
    ) -> None:
        """
        Инициализация CLI-приложения.

        :param analyzer_cls: Класс анализатора логов (по умолчанию LogAnalyzer).
        :param args: Объект Namespace для тестов (опционально).
        """
        self.filename: str | None = None
        self.analyzer_cls = analyzer_cls
        self.args = args or parse_args()
        self.keywords: list[str] = self._keywords()
        self.columns: list[str] = ["FILENAME"] + self.keywords + ["LINES"]
        logger.info(
            "CLI App инициализирована с аргументами: file=%s, keywords=%s",
            self.args.file,
            self.keywords,
        )

    def run(self) -> None:
        """
        Точка входа CLI. Обрабатывает аргументы.
        """
        file_path = Path(self.args.file)
        self.filename = file_path.name

        try:
            with file_path.open("r", encoding="utf-8") as f:
                lines = f.readlines()
        except OSError as e:
            print(f"Ошибка чтения файла: {e}")
            return
        self.start(lines)

    def start(self, data: list[str]) -> None:
        analyzer = self.analyzer_cls(data, self.keywords)
        result = analyzer.summary()
        logger.info("Результат анализа: %s", result)
        table = [
            tuple(
                [self.filename] + [result[k] for k in self.keywords] + [result["LINES"]]
            )
        ]
        print(tabulate(table, headers=self.columns, tablefmt="grid"))
        logger.info("Вывод таблицы завершён")

    def _keywords(self) -> list[str]:
        keywords = [kw.strip() for kw in self.args.keywords.split(",")]
        logger.debug("Парсинг ключевых слов: %s → %s", self.args.keywords, keywords)
        return keywords
