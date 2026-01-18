from abc import ABC, abstractmethod

class Button(ABC):

    def __init__(self,state = False):
        self.state = False

    def is_active(self):
        return self.state == True
    
    def set_active(self,state):
        self.state = state

    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    
    def render(self):
        print("Windows Button is rendering")

class MacButton(Button):
    
    def render(self):
        print("Mac Button is rendering")