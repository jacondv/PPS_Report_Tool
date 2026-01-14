class BaseController:
    def __init__(self):
        self._enabled = True

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False

    @property
    def enabled(self):
        return self._enabled

    @property
    def is_enable(self):
        return self._enabled