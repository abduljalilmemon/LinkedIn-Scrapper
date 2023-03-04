import sys
from loguru import logger


class Logger:
    __instance: logger = None

    def __init__(self, log_level='INFO'):
        if Logger.__instance is not None:
            raise Exception
        else:
            stdout_handler = dict(
                sink=sys.stdout,
                level=log_level,
                diagnose=False,
                filter=lambda record: record['level'].no < logger.level('ERROR').no,
                format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                       "<level>{level}</level> |"
                       "<cyan>{module}</cyan>:"
                       "<cyan>{function}</cyan>:"
                       "<cyan>{line}</cyan> - <level>{message}</level>"
            )
            stderr_handler = dict(
                sink=sys.stderr,
                level='ERROR',
                diagnose=False,
                format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                       "<level>{level}</level> |"
                       "<cyan>{module}</cyan>:"
                       "<cyan>{function}</cyan>:"
                       "<cyan>{line}</cyan> - <level>{message}</level>"
            )
            logger.configure(handlers=[stderr_handler, stderr_handler])
            Logger.__instance = logger

    @staticmethod
    def get_instance(log_level='INFO'):
        if Logger.__instance is None:
            Logger(log_level)
        return Logger.__instance
