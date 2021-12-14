# Чтобы произвести взаимоимпорты
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

load_dotenv()
#Здесь создается экземпляр бота
bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher(bot)