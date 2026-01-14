# utils/decorators.py

def only_if_enabled(func):
    """
    Decorator: chỉ chạy method nếu self.is_enable == True
    """
    def wrapper(self, *args, **kwargs):
        if not getattr(self, "is_enable", True):
            return
        return func(self, *args, **kwargs)
    return wrapper
