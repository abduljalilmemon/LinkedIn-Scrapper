from config import get_log_level
from .logger import Logger

logger = Logger.get_instance(get_log_level())
__all__ = ['logger']
