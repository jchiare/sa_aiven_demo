from datetime import datetime
from socket import gethostname


def get_UTC_time() -> datetime:
    return datetime.now().isoformat()


def get_host_name() -> str:
    return gethostname()
