from Task import Task


if __name__ == '__main__':

    task = Task("Fix-Integ test", "Vamsi")
    task.set_inprogress()
    task.done_task()
    task.reopen_task()