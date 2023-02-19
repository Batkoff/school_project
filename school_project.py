from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '6189442237:AAF-h3kAdQSstxLa5KD4kOmrBED-05Zhv68'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

knopka_1 = types.KeyboardButton('Вышивание крестиком')
knopka_2 = types.KeyboardButton('Бисероплетение')

greet_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(knopka_1)
greet_kb.add(knopka_2)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Приветик! Этот бот создан для развития твоих навыков в рукоделии.")
    await message.answer('Теперь выбери с чего именно ты хочешь начать обучение :)', reply_markup=greet_kb)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == 'Вышивание крестиком':
        await message.answer('https://youtu.be/mudMX4xnn0E', reply_markup=greet_kb)
    elif message.text == 'Бисероплетение':
        await message.answer('https://youtu.be/IMciaF4wQSU', reply_markup=greet_kb)
    else:
        await message.answer('чё', reply_markup=greet_kb)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)