from unittest.mock import MagicMock, patch

import pytest

from cli import App


@pytest.fixture
def fake_args(tmp_path):
    """Создаёт временный файл и поддельные аргументы CLI."""
    test_file = tmp_path / "log.txt"
    test_file.write_text("INFO first line\nERROR second line\nDEBUG third line\n")
    return MagicMock(file=str(test_file), keywords="INFO,ERROR,DEBUG")


def test_keywords_parsing(fake_args):
    """Проверяет, что ключевые слова парсятся корректно."""
    app = App(args=fake_args)
    assert app.keywords == ["INFO", "ERROR", "DEBUG"]
    assert "FILENAME" in app.columns
    assert "LINES" in app.columns


def test_run_reads_file_and_calls_start(fake_args):
    """Проверяет, что файл читается и вызывается start()."""
    mock_analyzer_cls = MagicMock()
    app = App(analyzer_cls=mock_analyzer_cls, args=fake_args)

    with patch.object(app, "start") as mock_start:
        app.run()
        mock_start.assert_called_once()
        args, _ = mock_start.call_args
        assert isinstance(args[0], list)
        assert len(args[0]) == 3  # три строки в тестовом файле


def test_run_file_not_found(fake_args, capsys):
    """Проверяет корректную обработку ошибки, если файл не существует."""
    fake_args.file = "no_such_file.log"
    app = App(args=fake_args)
    app.run()
    captured = capsys.readouterr()
    assert "Ошибка чтения файла" in captured.out


def test_start_prints_table(fake_args, capsys):
    """Проверяет вывод таблицы при успешной работе."""
    mock_analyzer = MagicMock()
    mock_analyzer.return_value.summary.return_value = {
        "INFO": 1,
        "ERROR": 1,
        "DEBUG": 1,
        "LINES": 3,
    }

    app = App(analyzer_cls=mock_analyzer, args=fake_args)
    app.filename = "log.txt"

    data = ["INFO one", "ERROR two", "DEBUG three"]
    app.start(data)

    output = capsys.readouterr().out
    assert "INFO" in output
    assert "ERROR" in output
    assert "LINES" in output
    assert "grid" not in output  # tabulate не пишет это слово, проверка по структуре
    mock_analyzer.assert_called_once_with(data, ["INFO", "ERROR", "DEBUG"])
