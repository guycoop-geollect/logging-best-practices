from helpers.logging_ import get_logger

_logger = get_logger(__name__)


def some_func(x):
    _logger.info(f"running my_func with value {x}")
    _logger.debug("debug")
