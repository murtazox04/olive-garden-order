from .base import *

env_type = config('ENV_TYPE')

if env_type == 'local':
    from .local import *
elif env_type == 'production':
    from .production import *
