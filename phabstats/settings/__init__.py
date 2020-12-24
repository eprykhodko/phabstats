import os

ENV = os.environ.get

PHAB_URL = ENV("PHAB_URL")
PHAB_TOKEN = ENV("PHAB_TOKEN")

SLACK_HOOK_URL = ENV("SLACK_HOOK_URL")


try:
    from .dev import *
except ImportError:
    pass
