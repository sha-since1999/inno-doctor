import os

IS_PRODUCTION = os.environ.get('IS_PRODUCTION', ' ') != 'False'
# IS_PRODUCTION = False
# print('IP', IS_PRODUCTION)

if IS_PRODUCTION:
    from .conf.production.settings import *
    print("Production Mode")
else:
    from .conf.development.settings import *
    print("Development Mode")