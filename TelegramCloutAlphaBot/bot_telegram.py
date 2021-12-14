from	aiogram.utils import executor

from create_bot import dp


# ФУНКЦИЯ при запуске бота
async def on_startup(_):
	print('Clout_Bot снова в Эфире!') #Чтобы запустить эту функцию, то ее необходимо передать в executor

from handlers import client, admin, other

#ЗАПУСКАЕМ ФУНКЦИИ

client.register_handlers_client(dp)
other.register_handlers_other(dp)

# ЗАПУСК БОТА
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)