# -------------------------------------------------
# A collection of all ai bots available for use in the game
#
# @author Joe Coleman
# -------------------------------------------------

# Add each new bot to this file to be used in the bot_test
# Be sure to also add the bot's constructor to the dictionary
from randombot import RandomBot
from attacbot import AttacBot 

>>>>>>> ae5134eb3243b2200db1ff3a8d5335afcad14553

class AiList(object):
    def __init__(self):
        self.bots = dict()
        self.bots['random'] = RandomBot
        self.bots['attac'] = AttacBot

    # Returns all available bots by name (key)
    def get_bot_names(self):
        return self.bots.keys()

    # Returns an instance of a specific bot
    def create_bot(self, name, map_weights, heuristic):
        bot = self.bots[name](map_weights, heuristic)
        return bot
