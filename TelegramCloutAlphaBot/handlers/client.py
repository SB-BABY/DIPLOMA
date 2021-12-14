from	aiogram import types, Dispatcher

from create_bot import dp, bot
######################################### - КЛИЕНТСКАЯ ЧАСТЬ - #########################################

# @dp.message_handler(commands=['start', 'help']) #Этот Хендлер сработает тогда
#Когда пользователь пишет \start, \help
#Или в тот момент, когда пользователь добавится к нашему боту

#Асинхронная функция
async def command_start(message : types.Message):
	#Если пользователь в группе, но не добавил БОТА, то делаем ИСКЛЮЧЕНИЕ
	try:
		# Код, который сработает во время команды Start & Help
		await bot.send_message(message.from_user.id, 'Добро пожаловать в CLOUT')
		await message.delete()
	except: 
		await message.reply('Чтобы начать общение с ботом - неоходимо ему написать:\nhttp://t.me/CloutAlphaBot')

	# Добавляем необходимые обработчики команд
#@dp.message_handler(commands=['price'])
async def clout_price_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Минимальное: 1500;\nСреднее: 3000;\nМаксимум: 5000;')

#@dp.message_handler(commands=['contact'])
async def clout_contact_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Наша почта:\ntest@test.com')

#Определяем функцию, в которой записать команды для регистрации handlera для бота и передать все эти функции в bot_telegram.py

def register_handlers_client(dp : Dispatcher ):
	dp.register_message_handler(command_start, commands=['start', 'help'])
	dp.register_message_handler(clout_price_command, commands=['price'] )
	dp.register_message_handler(clout_contact_command, commands=['contact'] )