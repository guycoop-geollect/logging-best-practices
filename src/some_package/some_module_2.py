from helpers.logging_ import get_logger

_logger = get_logger(__name__)


def some_func_2(y):
    _logger.info(f"running my_func_2 with value {y}")
    _logger.debug("debug")
