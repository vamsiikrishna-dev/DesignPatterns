from TaskState import IdleState, TaskState

class Task:

    def __init__(self, name, assignee):
        self.name = name
        self.assignee = assignee
        self.state: TaskState = IdleState()
        print("Task has been created in idle state")

    def set_inprogress(self):
        self.state.set_inprogress(self)

    def reopen_task(self):
        self.state.reopen_task(self)

    def done_task(self):
        self.state.done_task(self)

    def set_state(self, state: TaskState):
        self.state = state
    
    def get_state(self):
        return self.state
