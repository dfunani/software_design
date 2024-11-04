from abc import ABC, abstractmethod

class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class CutCommand(ICommand):
    def __init__(self, text_editor, start, end):
        self.text_editor = text_editor
        self.start = start
        self.end = end
        self.deleted_text = None

    def execute(self):
        self.deleted_text = self.text_editor.delete_text(self.start, self.end)
        return self.deleted_text

    def undo(self):
        self.text_editor.insert_text(self.start, self.deleted_text)


class CopyCommand(ICommand):
    def __init__(self, text_editor, start, end):
        self.text_editor = text_editor
        self.start = start
        self.end = end
        self.copied_text = None

    def execute(self):
        self.copied_text = self.text_editor.get_text(self.start, self.end)
        return self.copied_text

    def undo(self):
        pass  # Copying doesn't need to be undone


class PasteCommand(ICommand):
    def __init__(self, text_editor, start, text):
        self.text_editor = text_editor
        self.start = start
        self.text = text

    def execute(self):
        return self.text_editor.insert_text(self.start, self.text)

    def undo(self):
        return self.text_editor.delete_text(self.start, len(self.text))


class TextEditor:
    def __init__(self):
        self.text = ""
        self.command_history = []

    def insert_text(self, position, text):
        self.text = self.text[:position] + text + self.text[position:]
        return self.text

    def delete_text(self, start, end):
        deleted_text = self.text[start:end]
        self.text = self.text[:start] + self.text[end:]
        return deleted_text

    def get_text(self, start, end):
        return self.text[start:end]

    def execute_command(self, command: ICommand):
        self.command_history.append(command)
        return command.execute()

    def undo_command(self):
        if self.command_history:
            command = self.command_history.pop()
            command.undo()


# Example usage
text = "Hello, world!"
print(f"Given Text: {text}")

text_editor = TextEditor()
text_editor.insert_text(0, text)
print(f"New Text Editor: {text}")

cut_command = CutCommand(text_editor, 7, 12)
cut_text = text_editor.execute_command(cut_command)
print(f"Cut {cut_text} from {text} resulting {text_editor.text}")

paste_command = PasteCommand(text_editor, 0, cut_command.deleted_text)
paste_text = text_editor.execute_command(paste_command)
print(f"Pasted {cut_text} resulting {text_editor.text}")

text_editor.undo_command()  # Undoes the paste
print(f"Command Undone: {text_editor.text}")