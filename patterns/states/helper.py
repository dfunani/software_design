from datetime import datetime
from enum import Enum


class Levels(Enum):
    INFO = "info"
    DEBUG = "debug"


class Logger:  # Singleton Logger
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def info(self, message: str):
        self._log(Levels.INFO, message)

    def debug(self, message: str):
        self._log(Levels.DEBUG, message)

    def _log(self, level: Levels, message: str):
        print(
            f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {__name__} - {level.value} - {message}"
        )

class InvalidStateTransition(Exception):
    pass


class TransactionStates(Enum):
    DRAFT = "Draft"
    SUBMITTED = "Submitted"
    APPROVED = "Approved"
    ACTIVE = "Active"
    SETTLED = "Settled"
    REJECTED = "Rejected"
    CANCELLED = "Cancelled"