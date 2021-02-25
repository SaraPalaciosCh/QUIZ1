from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

class TurnOff(Command):

    def execute(self):
        print("Deleting tasks...")
        print("Turning off")

class Talk(Command):

    def execute(self):
        print("Talking...bla bla bla....")

class Sleep(Command):

    def execute(self):
        print("Im going to take a nap")

class TurnOn(Command):

    def execute(self):
        print("I'm On and I'm going to do something cool")
        




