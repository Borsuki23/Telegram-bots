import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5579061130:AAEiIBroucLkh0b6xarE52m81zH9XsyA_Hk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text*10)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)