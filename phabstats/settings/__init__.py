import os

ENV = os.environ.get

PHAB_URL = ENV('PHAB_TOKEN')
PHAB_TOKEN = ENV('PHAB_TOKEN')

SLACK_HOOK_ULR = ENV('SLACK_HOOK_ULR')


try:
    from .dev import *
except ImportError:
    pass

