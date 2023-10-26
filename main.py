from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '6620613217:AAHn7cDxXc73e6Qx49Wl2OY6BeDJnQgYF-A'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ Эхо-бот от Skillbox!\nОтправь мне любое сообщение, а я тебе обязательноотвечу.") #Так как код работает асинхронно, то обязательно пишем await.