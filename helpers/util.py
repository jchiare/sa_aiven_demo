from datetime import datetime
from socket import gethostname
from typing import Text


def get_UTC_time() -> datetime:
    return datetime.now().isoformat()


def get_host_name() -> Text:
    return gethostname()
