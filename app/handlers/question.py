from aiogram import Dispatcher, types
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

cb_question = CallbackData("fabnum", "action")


class Question(StatesGroup):
    question_state1 = State()
    question_state2 = State()


async def question_main_handler(call: types.CallbackQuery):

    await Question.question_state1.set()

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text="Связаться с сервисным центром",
                                            callback_data=cb_question.new(action="question2")))
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data=cb_question.new(action="question1")))

    await call.message.edit_text("Напиши свой вопрос:", reply_markup=keyboard)
    await call.answer()


async def question_ok_mhandler(message: types.Message, state: FSMContext):

    await state.reset_state(with_data=False)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data=cb_question.new(action="question4")))

    await message.answer("""Спасибо за обращение! Ваш вопрос отправлен в Сервисный центр. \
В скором времени с Вами свяжется наш сотрудник.""", reply_markup=keyboard)


async def question_service_handler(call: types.CallbackQuery):

    await Question.question_state2.set()

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data=cb_question.new(action="question3")))

    await call.message.edit_text("""Вы можете связаться с Сервисным центром компании по телефону +7 ХХХ ХХХ ХХХХ. \
Время работы Пн.-Пт. с 10-00 до 19-00, Сб., Вс. выходные дни.""", reply_markup=keyboard)
    await call.answer()


def register_handlers_question(dp: Dispatcher):
    dp.register_callback_query_handler(question_main_handler, cb_question.filter(action="auth21"),
                                       state="*")

    dp.register_message_handler(question_ok_mhandler, state=Question.question_state1)

    dp.register_callback_query_handler(question_service_handler, cb_question.filter(action="question2"),
                                       state="*")
