from .heroku import *
try:
    from .local import *
except ImportError:
    pass
