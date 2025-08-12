import logging
from colorama import Fore, Style, init
from utils._context import ctx

init(autoreset=True)


def get_logger() -> logging.Logger:
    level_styles = {
        "DEBUG": (Fore.CYAN, "🐞"),
        "INFO": (Fore.GREEN, "ℹ️"),
        "WARNING": (Fore.YELLOW, "⚠️"),
        "ERROR": (Fore.RED, "❌"),
        "CRITICAL": (Fore.LIGHTRED_EX, "🔥")
    }

    class EmojiColorFormatter(logging.Formatter):
        def format(self, record):
            color, emoji = level_styles.get(record.levelname, (Fore.WHITE, ""))
            record.levelname = f"{emoji} {record.levelname}"
            message = super().format(record)
            return f"{color}{message}{Style.RESET_ALL}"

    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, ctx.log_level))
    logger.propagate = False
    logger.handlers.clear()

    formatter = EmojiColorFormatter(
        "%(asctime)s: %(levelname)-10s %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


if __name__ == "__main__":


    log = get_logger()

    log.info("Info message")
    log.error("Error message")
    log.debug("Debug message")
    log.warning("Warn Message")
