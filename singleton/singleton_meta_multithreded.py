from threading import Lock

"""
Эта реализация Singletone, который можно
использовать в многопоточном приложении
"""


class ChocolateBoilerMeta(type):
    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class ChocolateBoiler(metaclass=ChocolateBoilerMeta):
    def __init__(self):
        self.empty = True
        self.boiled = False

    def fill(self):
        if self.is_empty():
            self.empty = False
            self.boiled = False

    def drain(self):
        if not self.is_empty() and self.is_boiled():
            self.empty = True

    def boil(self):
        if not self.is_empty() and not self.is_boiled():
            self.boiled = True

    def is_empty(self):
        return self.empty

    def is_boiled(self):
        return self.boiled


s1 = ChocolateBoiler()
s2 = ChocolateBoiler()

print(id(s1))
print(id(s2))
