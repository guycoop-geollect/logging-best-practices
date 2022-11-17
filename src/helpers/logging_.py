import logging
import os
import sys


def setup_logging(name: str = None) -> logging.Logger:
    """Sets up and returns a logger.

    :param name: Name to use for logger.
    :return: Configured logger."""
    # get logger
    logger = logging.getLogger(name=name)

    # add handlers and formatting
    for h in logger.handlers:
        logger.removeHandler(hdlr=h)
    ch = logging.StreamHandler(stream=sys.stdout)
    console_formatter = logging.Formatter(
        fmt="%(asctime)s.%(msecs)3d-%(name)-12s: %(levelname)-8s %(message)s"
    )
    ch.setFormatter(fmt=console_formatter)
    logger.addHandler(hdlr=ch)

    # set level
    loglevel = os.getenv(key=f"LOGLEVEL_{name.upper()}")  # name specific
    if loglevel is None:
        loglevel = os.getenv(key="LOGLEVEL", default="INFO")  # otherwise global
    loglevel = getattr(logging, loglevel.upper())
    logger.setLevel(level=loglevel)

    return logger
