from enum import Enum


class StatusCodes(Enum):
    OK = "OK"
    CLIENT_ERROR = "Client error"
    INTERNAL_ERROR = "Internal error"
