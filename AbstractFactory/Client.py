from AbstractFactory import WindowsFactory, MacFactory
from Utils import OSType

os = OSType.Mac #usually it comes from config file of the system

if __name__ == "__main__":

    gui_factory = MacFactory() if os == OSType.Mac else WindowsFactory()

    button = gui_factory.create_button()
    checkbox = gui_factory.create_checkbox()
    button.render()
    checkbox.render() 