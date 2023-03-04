import logging

from environs import Env

env = Env()
WORKER_ENV = env('WORKER_ENV', 'local')
if WORKER_ENV == 'local':
    env.read_env()

DEBUG = env.bool('DEBUG', False)
EMAIL = env.bool('EMAIL')
PASSWORD = env.bool('PASSWORD')


def get_log_level():
    return logging.DEBUG if DEBUG else logging.INFO