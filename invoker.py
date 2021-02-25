
from comands import Command

class Invoker:

    _task = None
    _last_task = None


    def set_task(self, command: Command):
        self._task = command

    def set_last_task(self, command: Command):
        self._last_task= command

    def do_something_important(self):
        print("BOT: Ready to start...")
        if isinstance(self._task, Command):
            self._task.execute()

        print("BOT: ...anything else??")

        if isinstance(self._last_task, Command):
            self._last_task.execute()