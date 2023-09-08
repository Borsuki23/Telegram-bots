from aiogram import Bot, Dispatcher, executor, types

from decouple import config

bot = Bot(config('5579061130:AAEiIBroucLkh0b6xarE52m81zH9XsyA_Hk'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привіт, я допоможу тобі порахувати А + Б = ?")
                        
@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.answer("Напиши мені: 2 + 2")
    
@dp.message_handler()
async def echo(message: types.Message):
    try:
        a, b = message.text.split('+')
        await message.answer(int(a) + int(b))
    except:
        await message.answer("Напиши мені: 2 + 2")
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
