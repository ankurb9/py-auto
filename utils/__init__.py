from ._log import get_logger
from ._context import Context

log = get_logger()
ctx = Context()

__all__ = ["log", "ctx"]