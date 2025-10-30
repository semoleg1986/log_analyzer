from utils.logger import get_logger

logger = get_logger(__name__)


class LogAnalyzer:
    """Анализатор логов для подсчёта ошибок, предупреждений и строк."""

    def __init__(self, data: list[str], keywords: list[str]) -> None:
        """
        Инициализация анализатора логов.

        :param data: Список строк лог-файла.
        :type data: list[str]
        :param keywords: Список ключевых слов для подсчёта.
        :type keywords: list[str]
        """
        self.data = data
        self.keywords = keywords
        logger.info(
            "LogAnalyzer инициализирован с %d строками и ключевыми словами: %s",
            len(data),
            ", ".join(keywords),
        )

    @property
    def lines(self) -> int:
        """Количество строк."""
        return len(self.data)

    def count_by_keyword(self, keyword: str) -> int:
        """
        Подсчитывает количество строк, содержащих указанное слово (без учёта регистра).

        :param keyword: Ключевое слово для поиска.
        :type keyword: str
        :return: Количество строк с указанным словом.
        :rtype: int
        """
        count = sum(1 for line in self.data if keyword.lower() in line.lower())
        logger.info("Подсчитано %d строк для ключевого слова '%s'", count, keyword)
        return count

    def summary(self) -> dict[str, int]:
        """
        Возвращает словарь с результатами анализа.

        :return: словарь
        :rtype: dict[str, int]
        """
        result = {kw: self.count_by_keyword(kw) for kw in self.keywords}
        result["LINES"] = self.lines
        logger.info("Итоговый summary: %s", result)
        return result
