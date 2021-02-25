from comands import *
from invoker import Invoker

Talk = Talk()
TurnOn = TurnOn()
Sleep = Sleep()


bot = Invoker()
bot.set_task(TurnOn)
bot.set_last_task(Sleep)

bot.do_something_important()




