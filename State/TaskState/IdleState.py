from .TaskState import TaskState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Task import Task

class IdleState(TaskState):
    '''
        This is the state when we create a new task. it will be in idlestate by default.
    '''

    def set_inprogress(self, task: 'Task'):
        from .ProgressState import ProgressState
        print("Setting the task in progress.")
        task.state = ProgressState()
        

    def reopen_task(self, task: 'Task'):
        print("Task is in progress. can't reopen as open task.")

    def done_task(self, task: 'Task'):
        print("Can't done a idle task. make it to inprogress first.")
        
        
    