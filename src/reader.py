import os
from typing import Any
import logging
import pandas as pd
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent

reader_logger = logging.getLogger("reader")
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s - %(pathname)s - %(pathname)s:%(lineno)d")
console_handler.setFormatter(console_formatter)
file_handler = logging.FileHandler(os.path.join(ROOT_DIR, "logs", "reader.log"), "w")
file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s -%(name)s - %(message)s - %(pathname)s:%(lineno)d")
file_handler.setFormatter(file_formatter)
reader_logger.addHandler(file_handler)
reader_logger.addHandler(console_handler)
reader_logger.setLevel(logging.DEBUG)

def transaction_reader(file_path: str = "") -> Any:
    """
    Загружает данные о транзакциях из Excel - файла.

    :param file_path: Путь к Excel - файлу.
    :return: DataFrame с транзакциями.
    """
    try:
        data = pd.read_excel(file_path)
    except Exception:
        reader_logger.warning(Exception)
        raise Exception
    reader_logger.info("Успешно")
    return data