from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from VisitorUtil import Visitor

class Product(ABC):

    @abstractmethod
    def accept(self, visitor: 'Visitor'):
        pass
