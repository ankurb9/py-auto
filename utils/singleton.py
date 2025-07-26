

def singleton(cls):
    """
    A decorator that converts a class into a Singleton.
    Only one instance of the class will ever exist.
    """
    instances = {}  # Stores singleton instances

    def get_instance(*args, **kwargs):
        # If the class hasn't been instantiated yet, create it
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]  # Return the existing instance

    return get_instance