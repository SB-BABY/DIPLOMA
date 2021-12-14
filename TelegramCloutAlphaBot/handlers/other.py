from	aiogram import types, Dispatcher
from create_bot import dp

import  json, string

######################################### - ОБЩАЯ ЧАСТЬ - #########################################
# @dp.message_handler()
async def echo_send(message : types.Message):
	#ПИШЕМ ФИЛЬТР МАТОВ
	#ИСПОЛЬЩУЕМ ГЕНЕРАТОР МНОЖЕСТВ
	# чтобы человек не могу замаскрировать слова знаками пункутациями, то уюерем их с помощью функции  
	# получаем сообщение, разбиваем по разделителю, получается список из слов, проходимся циклом for и каждое слово обрабатывает
	if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
		.intersection(set(json.load(open('cenz.json')))) != set():
		await message.reply('Маты запрещены! Уважайте друг друга <3')
		await message.delete()

def register_handlers_other(dp : Dispatcher ):
	dp.register_message_handler(echo_send)