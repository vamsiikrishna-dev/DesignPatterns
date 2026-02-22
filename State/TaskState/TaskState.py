from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Task import Task

class TaskState(ABC):

    @abstractmethod
    def set_inprogress(self, task: 'Task'):
        pass

    @abstractmethod
    def reopen_task(self, task: 'Task'):
        pass

    @abstractmethod
    def done_task(self, task: 'Task'):
        pass

