from aiogram import Dispatcher, types
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

cb_error = CallbackData("fabnum", "action")


class Error(StatesGroup):
    error_state1 = State()


async def error_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(with_data=False)

    keyboard = types.InlineKeyboardMarkup(row_width=4)
    buttons = [
        types.InlineKeyboardButton(text="Error 303", callback_data=cb_error.new(action="error1")),
        types.InlineKeyboardButton(text="Error 304", callback_data=cb_error.new(action="error2")),
        types.InlineKeyboardButton(text="Error 305", callback_data=cb_error.new(action="error3")),
        types.InlineKeyboardButton(text="Error 306", callback_data=cb_error.new(action="error4")),
        types.InlineKeyboardButton(text="Error 307", callback_data=cb_error.new(action="error5")),
        types.InlineKeyboardButton(text="Error 308", callback_data=cb_error.new(action="error6")),
        types.InlineKeyboardButton(text="Error 309", callback_data=cb_error.new(action="error7")),
        types.InlineKeyboardButton(text="Error 310", callback_data=cb_error.new(action="error8")),
        types.InlineKeyboardButton(text="Error 311", callback_data=cb_error.new(action="error9")),
        types.InlineKeyboardButton(text="Error 360", callback_data=cb_error.new(action="error10")),
        types.InlineKeyboardButton(text="Меню", callback_data=cb_error.new(action="error11"))
    ]
    keyboard.add(*buttons)

    await call.message.edit_text("""В целях мониторинга технического состояния и реализации протоколов безопасности \
в аппарате предусмотрена развернутая система диагностики. Если у Вас на аппарате возникло сообщение об ошибке, \
то вы сможете уточнить описание ошибки и рекомендации по дальнейшим действиям. \
Выберите код ошибки указанный в сообщении.""", reply_markup=keyboard)
    await call.answer()


async def error_303to307_handler(call: types.CallbackQuery, callback_data: dict):
    action = callback_data["action"]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Связаться с сервисным центром", callback_data=cb_error.new(action="error13")),
        types.InlineKeyboardButton(text="Назад", callback_data=cb_error.new(action="error12"))
    ]
    keyboard.add(*buttons)

    if action == "error1":
        str = "Ошибка №303\nОшибка запроса ID манипулы. Необходимо обратиться в Сервисный центр."
    elif action == "error2":
        str = "Ошибка №304\nОшибка датчика скорости. Необходимо обратиться в Сервисный центр."
    elif action == "error3":
        str = "Ошибка №305\nОшибка связи аппарата с манипулой. Необходимо обратиться в Сервисный центр."
    elif action == "error4":
        str = "Ошибка №306\nОшибка работы microSD карты или SPI flash. Необходимо обратиться в Сервисный центр."
    elif action == "error5":
        str = "Ошибка №307\nОшибка связи с контроллером Touch Screen. Необходимо обратиться в Сервисный центр."

    await call.message.edit_text(str, reply_markup=keyboard)
    await call.answer()


async def error_308to311_handler(call: types.CallbackQuery, callback_data: dict):
    action = callback_data["action"]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Получить консультацию специалиста",
                                   callback_data=cb_error.new(action="error16")),
        types.InlineKeyboardButton(text="Назад", callback_data=cb_error.new(action="error15"))
    ]
    keyboard.add(*buttons)

    if action == "error6":
        str = "Ошибка №308\nПредупреждение о слишком высокой температуре   двигателя. Необходимо охладить манипулу."
    elif action == "error7":
        str = "Ошибка №309\nПредупреждение о перегреве двигателя. Необходимо охладить манипулу."
    elif action == "error8":
        str = "Ошибка №310\nПредупреждение о высокой температуре MCU манипулы. Необходимо охладить манипулу."
    elif action == "error9":
        str = "Ошибка №311\nПредупреждение о перегреве MCU манипулы. Необходимо охладить манипулу."

    await call.message.edit_text(str, reply_markup=keyboard)
    await call.answer()


async def error_service_handler(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data=cb_error.new(action="error14")))

    await call.message.edit_text("""Мы сожалеем, что Вы столкнулись со технической неисправностью оборудования. \
Мы постараемся исправить данную ситуацию в кратчайшие сроки. Информация о данной ситуации автоматически \
сформирована и направлена в Сервисный центр. В ближайшее время с Вами свяжется наш сотрудник.
Вы можете связаться с Сервисным центром компании по телефону +7 ХХХ ХХХ ХХХХ. 
Время работы Пн.-Пт. с 10-00 до 19-00, Сб., Вс. выходные дни.""", reply_markup=keyboard)
    await call.answer()


async def error_consult_handler(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data=cb_error.new(action="error17")))

    await call.message.edit_text("""Спасибо за обращение. Запрос на консультацию направлен в Сервисный центр. \
В ближайшее время с Вами свяжется наш сотрудник.""", reply_markup=keyboard)
    await call.answer()


async def error_360_handler(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_error.new(action="error18")))

    await call.message.edit_text("""Ошибка №360
Блокировка аппарата из-за превышения допустимого \
пикового тока двигателя манипулы. Аппарат временно заблокирован. Для снятия блокировки необходимо \
ввести код безопасности.
Введите код запроса с экрана аппарат""", reply_markup=keyboard)
    await Error.error_state1.set()
    await call.answer()


async def error_put_handler(message: types.Message):

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(text="Если код не сработал", callback_data=cb_error.new(action="error19")),
        types.InlineKeyboardButton(text="Да", callback_data=cb_error.new(action="error20"))
    ]
    keyboard.add(*buttons)

    await message.answer('''Код для разблокировки аппарата:\nХХХХХ
Пожалуйста, введите его в соответствующе поле\nАппарат разблокирован?''', reply_markup=keyboard)


async def error_code_handler(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(with_data=False)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="К списку ошибок", callback_data=cb_error.new(action="error21")))

    await call.message.edit_text("""Мы сожалеем, что Вы столкнулись с невозможностью снять блокировку аппарата. \
Мы постараемся исправить данную ситуацию в кратчайшие сроки. Информация о данной ситуации автоматически \
сформирована и направлена в Сервисный центр. В ближайшее время с Вами свяжется наш сотрудник
Вы можете связаться с Сервисным центром компании по телефону +7 ХХХ ХХХ ХХХХ. \
Время работы Пн.-Пт. с 10-00 до 19-00, Сб., Вс. выходные дни.""", reply_markup=keyboard)
    await call.answer()


async def error_ok_handler(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(with_data=False)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data=cb_error.new(action="error22")))

    await call.message.edit_text("""В дальнейшим, для предотвращения выхода их строя агрегатов аппарата просьба \
руководствоваться следующими рекомендациями:\n1. Не допускать попадания посторонних предметов в манипулу
2. Обслуживать массажный барабан в соответствии с рекомендациями производителя
3. Не допускать чрезмерного механического воздействия на на манипулу
Обращаем ваше внимание, что при многократной блокировки манипулы в отчетный период, которые возникли в \
следствие неверной эксплуатации, гарантия производителя на аппарат может быть аннулирована.
Отчет о текущей ситуации направлен в Сервисный центр для повышения качества обслуживания. \
Спасибо.""", reply_markup=keyboard)
    await call.answer()


def register_handlers_error(dp: Dispatcher):
    dp.register_callback_query_handler(error_menu_handler, cb_error.filter(action=["auth17", "error12", "error15",
                                                                                   "error18", "error21"]), state="*")
    dp.register_callback_query_handler(error_303to307_handler, cb_error.filter(action=["error1", "error2", "error3",
                                                                                       "error4", "error5"]))
    dp.register_callback_query_handler(error_308to311_handler, cb_error.filter(action=["error6", "error7",
                                                                                       "error8", "error9"]))
    dp.register_callback_query_handler(error_service_handler, cb_error.filter(action="error13"))
    dp.register_callback_query_handler(error_consult_handler, cb_error.filter(action="error16"))
    dp.register_callback_query_handler(error_360_handler, cb_error.filter(action=["error10"]), state="*")
    dp.register_message_handler(error_put_handler, state=Error.error_state1)
    dp.register_callback_query_handler(error_code_handler, cb_error.filter(action="error19"), state="*")
    dp.register_callback_query_handler(error_ok_handler, cb_error.filter(action="error20"), state="*")








