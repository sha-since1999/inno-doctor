import os

IS_PRODUCTION = os.environ.get('IS_PRODUCTION', ' ') != 'False'
# IS_PRODUCTION = False
# IS_PRODUCTION = os.environ.get('IS_PRODUCTION') or False

if IS_PRODUCTION:
    from .conf.production.settings import *
else:
    from .conf.development.settings import *
 