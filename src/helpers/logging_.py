import logging
import os
import sys


def get_logger(name: str = None) -> logging.Logger:
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

    # - set level - #
    # set level on a module/package wise basis
    # starting with most specific name i.e. PACKAGE.PACKAGE.MODULE, then PACKAGE.PACKAGE, then PACKAGE, etc.
    loglevel = None
    split_name = name.split(".")
    for i in range(len(split_name), 0, -1):
        env_name = ".".join([n.upper() for n in split_name[0:i]])
        loglevel = os.getenv(key=f"LOGLEVEL_{env_name}")
        if loglevel is not None:
            break

    # otherwise use the global log level
    if loglevel is None:
        loglevel = os.getenv(key="LOGLEVEL", default="INFO")

    loglevel = getattr(logging, loglevel.upper())
    logger.setLevel(level=loglevel)

    return logger
