from .EnvFileError import EnvFileError


class KeyUnknownError(EnvFileError):
    def __init__(self, key, message, *args, **kwargs):
        super().__init__(message, args, kwargs)
        self.key = key
