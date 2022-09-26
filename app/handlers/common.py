from aiogram import Dispatcher, types


async def common_income_handler(message: types.Message):
    await message.reply("""На данном этапе нужно использовать только кнопки. Либо нажмите /start, \
чтобы начать с начала""")


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(common_income_handler, content_types=types.ContentType.ANY, state="*")
