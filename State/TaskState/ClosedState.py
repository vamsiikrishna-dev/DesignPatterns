from .TaskState import TaskState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Task import Task

class ClosedState(TaskState):
        
    '''
        This is state when the task is closed.
    '''

    def set_inprogress(self, task: 'Task'):
        print("Can't set task in progress. please re-open it first.")
        return

    def reopen_task(self, task: 'Task'):
        from .IdleState import IdleState
        print("Reopening the task.")
        task.state = IdleState()

    def done_task(self, task: 'Task'):
        print("No point of closing the closed task.")

        