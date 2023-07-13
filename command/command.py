from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class noCommand(Command):
    def execute(self):
        print("No command")


class RemoteControl:
    def __init__(self):
        self.on_commands: list(Command) = [noCommand() for _ in range(7)]
        self.off_commands: list(Command) = [noCommand() for _ in range(7)]

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int):
        self.on_commands[slot].execute()

    def off_button_was_pushed(self, slot: int):
        self.off_commands[slot].execute()

    def __str__(self):
        output = []
        output.append("\n------ Remote Control -------\n")
        for i in range(len(self.on_commands)):
            output.append(
                (
                    f"[slot {i}] {self.on_commands[i].__class__.__name__}    "
                    f"{self.off_commands[i].__class__.__name__}\n"
                )
            )
        return "".join(output)


class Light:
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()
