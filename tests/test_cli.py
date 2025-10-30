from core.analyzer import LogAnalyzer

MOCK_LOGS = [
    "INFO Starting process",
    "WARNING Disk space low",
    "ERROR File not found",
    "error timeout",
    "INFO Done",
]


def test_count_by_keyword():
    analyzer = LogAnalyzer(MOCK_LOGS, ["ERROR", "WARNING"])
    assert analyzer.count_by_keyword("ERROR") == 2
    assert analyzer.count_by_keyword("WARNING") == 1
    assert analyzer.lines == 5


def test_summary():
    analyzer = LogAnalyzer(MOCK_LOGS, ["ERROR", "WARNING"])
    result = analyzer.summary()
    assert result == {"ERROR": 2, "WARNING": 1, "LINES": 5}
