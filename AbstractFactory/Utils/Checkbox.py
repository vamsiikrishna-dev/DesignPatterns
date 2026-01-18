from abc import ABC, abstractmethod

class Checkbox(ABC):

    def __init__(self,state = False):
        self.state = False

    def is_active(self):
        return self.state == True
    
    def set_active(self,state):
        self.state = state

    @abstractmethod
    def render(self):
        pass

class WindowsCheckbox(Checkbox):
    
    def render(self):
        print("Windows Checkbox is rendering")

class MacCheckbox(Checkbox):
    
    def render(self):
        print("Mac Checkbox is rendering")