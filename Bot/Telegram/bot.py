from Bot.Model import config

from telebot import TeleBot

class Bot(TeleBot):
   def __init__(self, token: str, *args, **kwargs):
        super().__init__(token=config.BOT_TOKEN, *args, **kwargs)
