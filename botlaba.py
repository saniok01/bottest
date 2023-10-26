from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup

API_TOKEN = '6620613217:AAHn7cDxXc73e6Qx49Wl2OY6BeDJnQgYF-A'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ БФУ-бот помощник по кластерам\nВыбери, про какой кластер ты хочешь узнать.")
    bot.send_photo(message.chat.id, photo="https://sun9-12.userapi.com/impg/1zCF3IhajAXF4HEooMMDV-uwAlqLQ2dUBSTnAg/KKQXZRH10Qw.jpg?size=2560x1809&quality=95&sign=bfb1489f5c7cb60ed1bb7bde37ff77bf&type=album", caption='Всего в БФУ 4 научных кластера (института), а в них входит 13 Высших школ. Также есть университетский колледж, но он не относится к научным кластерам и ВШ.')
    greet_kb = ReplyKeyboardMarkup(row_width=1)

    a1 = types.KeyboardButton(text="Институт управления и территориального развития")
    a2 = types.KeyboardButton(text="Институт высоких технологий")
    a3 = types.KeyboardButton(text="Институт медицины и науки о жизни (МЕДБИО)")
    a4 = types.KeyboardButton(text="Институт образования и гуманитарных наук")
    greet_kb.add(a1, a2, a3, a4)
@dp.message_handler()
async def otvet(message: types.Message):
    if "Институт управления и территориального развития" in message.text:
        await message.answer ("Институт управления и территориального развития включает в себя следующие высшие школы: Высшая школа бизнеса и предпринимательства.\n Высшая школа права.\n Высшая школа гострепреимства.")
        types.KeyboardButton(text="Назад")
    if "Институт высоких технологий" in message.text:
        await message.answer('Институт высоких технологий включает в себя следующие высшие школы: Высшая кшола компьютерных наук и прикладной математики\n Высшая школа физических проблем и технологий\n Высшая школа междисциплинарных исследований и инжиниринга\\' )
        types.KeyboardButton(text="Назад")
    if "Институт медицины и науки о жизни (МЕДБИО)" in message.text:
        await message.answer('Институт медицины и науки о жизни (МЕДБИО) включает в себя следующие высшие школы: Высшая школа медицины\n Высшая школа живых систем', )
    if "Институт образования и гуманитарных наук.." in message.text:
        await message.answer('Институт образования и гуманитарных наук включает в себя следующие высшие школы: Высшая школа образования и психологии\n Высшая школа филологии кросс-культурной коммуникации\n Высшая школа медиа и дизайна\n Высшая школа физической культуры и спорта\n Высшая школа философии, истории и социальных наук' )

    if "Назад" in message.text:
        greet_kb = ReplyKeyboardMarkup(row_width=1)
        a1 = types.KeyboardButton(text="Институт управления и территориального развития")
        a2 = types.KeyboardButton(text="Институт высоких технологий")
        a3 = types.KeyboardButton(text="Институт медицины и науки о жизни (МЕДБИО)")
        a4 = types.KeyboardButton(text="Институт образования и гуманитарных наук")
        greet_kb.add(a1, a2, a3, a4)

        await message.reply('Главное меню1.',
                            reply_markup=greet_kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
