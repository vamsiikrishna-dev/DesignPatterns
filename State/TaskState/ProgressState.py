from .TaskState import TaskState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Task import Task

class ProgressState(TaskState):
        

    def set_inprogress(self, task: 'Task'):
        print("Already in progress. No point of making in progress again.")

    def reopen_task(self, task: 'Task'):
        print("Can't reopen an open task.")

    def done_task(self, task: 'Task'):
        from .ClosedState import ClosedState
        task.state = ClosedState()

    