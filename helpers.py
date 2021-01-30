from datetime import datetime
import socket

def get_UTC_time() -> datetime:
    return datetime.now().isoformat()

def get_host_name() -> str:
    return socket.gethostname()