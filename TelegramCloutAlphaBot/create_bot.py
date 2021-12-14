# Чтобы произвести взаимоимпорты
from	aiogram import Bot
from	aiogram.dispatcher import Dispatcher
import os

#Здесь создается экземпляр юота
bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher(bot)