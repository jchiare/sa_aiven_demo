# Utility functions

from datetime import datetime
from socket import gethostname
from typing import Text


def get_UTC_time() -> datetime:
    """
    Returns current time in UTC
    """
    return datetime.now().isoformat()


def get_host_name() -> Text:
    """
    Returns the host name of the machine calling this function
    - compatible with Linux, Mac, and Windows
    """
    return gethostname()
