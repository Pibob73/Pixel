from abc import ABC, abstractmethod


class UnitABC(ABC):
    @abstractmethod
    def superimposer(self):
        return self.back_object

    @property
    def back_object(self):
        return self.back_object

    @property
    def head(self):
        return self.head


