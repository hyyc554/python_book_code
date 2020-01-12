from loguru import logger

logger.debug("That's it, beautiful and simple logging!")

logger.add("output.log", backtrace=True, diagnose=True)  # Set 'False' to not leak sensitive data in prod


def func(a, b):
    return a / b


def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")


nested(0)
