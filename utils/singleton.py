import threading

def singleton(cls):
    """
    A thread-safe decorator that converts a class into a Singleton.
    Only one instance of the class will ever exist.
    """
    instances = {}
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        with lock:
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance