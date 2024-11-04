from typing import List

class IComponent:
    """ Interface for GUI components """
    pass

class Window(IComponent):
    """ Represents a window in the GUI """

    __components: List[IComponent] = []

    def __init__(self, title: str):
        self.title = title

    @property
    def components(self) -> List[IComponent]:
        return self.__components

    def add_component(self, component: IComponent):
        self.__components.append(component)

    def show(self):
        print(f"Showing window: {self.title}")

    def hide(self):
        print(f"Hiding window: {self.title}")


class Button(IComponent):
    """ Represents a button in the GUI """

    def __init__(self, text: str):
        self.text = text

    def click(self):
        print(f"Button '{self.text}' clicked")


class Label(IComponent):
    """ Represents a label in the GUI """

    def __init__(self, text: str):
        self.text = text

    def set_text(self, text: str):
        self.text = text


class GUIFacade:
    """ Facade for creating and managing the user interface """

    def __init__(self):
        self.window = Window("My Application")
        self.button = Button("Click Me")
        self.label = Label("Hello, World!")

    def create_ui(self):
        self.window.show()
        self.window.add_component(self.button)
        self.window.add_component(self.label)

    def handle_button_click(self):
        self.button.click()


# Usage:
gui_facade = GUIFacade()
gui_facade.create_ui()
gui_facade.handle_button_click()