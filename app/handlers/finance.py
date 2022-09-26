from aiogram import Dispatcher, types
from aiogram.utils.callback_data import CallbackData

cb_finance = CallbackData("fabnum", "action")


async def finance_menu_handler(call: types.CallbackQuery):

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data=cb_finance.new(action="finance1")))
    keyboard.add(types.InlineKeyboardButton(text="Если код не сработал",
                                            callback_data=cb_finance.new(action="finance2")))
    keyboard.add(types.InlineKeyboardButton(text="Причины блокировки",
                                            callback_data=cb_finance.new(action="finance3")))
    keyboard.add(types.InlineKeyboardButton(text="Что делать?",
                                            callback_data=cb_finance.new(action="finance4")))
    keyboard.add(types.InlineKeyboardButton(text="Как ввести код?",
                                            callback_data=cb_finance.new(action="finance5")))

    await call.message.edit_text("""Финансовая блокировка:
 - Почему оборудование заблокировано?
 - Что делать в этом случае?
 - Как ввести код разблокировки?""", reply_markup=keyboard)
    await call.answer()


async def finance_reason_handler(call: types.CallbackQuery):

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data=cb_finance.new(action="finance8")))
    keyboard.add(types.InlineKeyboardButton(text="Что делать?",
                                            callback_data=cb_finance.new(action="finance9")))

    await call.message.edit_text("""Финансовая блокировка оборудования возникает при нарушений соответствующих условия \
вашего договора. Такая ситуация может возникнуть в нескольких случаях:
1. нарушены фин. условия договора
2. период действия текущего договора истек
3. Нарушены иные условия договора
4. Не верно настроена дата и время на аппарате""", reply_markup=keyboard)
    await call.answer()


async def finance_resolve_handler(call: types.CallbackQuery):

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_finance.new(action="finance10")))
    keyboard.add(types.InlineKeyboardButton(text="Направить заявку",
                                            callback_data=cb_finance.new(action="finance12")))
    keyboard.add(types.InlineKeyboardButton(text="Как связаться?",
                                            callback_data=cb_finance.new(action="finance13")))

    await call.message.edit_text("""Подготовьте следующую информацию для общения с отделом продаж:
1. № договора и дату заключения
2. Модель аппарата
3. Серийный номер аппарата
4. Показания часов и даты на аппарате
Для решения возникшей ситуации вам нужно обратиться в отдел продаж компании.""", reply_markup=keyboard)
    await call.answer()


async def finance_code_handler(call: types.CallbackQuery):

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data=cb_finance.new(action="finance6")))

    await call.message.edit_text("""Мы сожалеем, что Вы столкнулись со сложностями разблокировки аппарата. \
Мы постараемся исправить данную ситуацию в кратчайшие сроки. Информация о данной ситуации автоматически \
сформирована и направлена в Сервисный центр. В ближайшее время с Вами свяжется наш сотрудник.\
\
Вы можете связаться с Сервисным центром компании по телефону +7 ХХХ ХХХ ХХХХ. \
Время работы Пн.-Пт. с 10-00 до 19-00, Сб., Вс. выходные дни.""", reply_markup=keyboard)
    await call.answer()


async def finance_info_handler(call: types.CallbackQuery):

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_finance.new(action="finance7")))

    await call.message.edit_text("""НАПИСАТЬ!!!\n
Инструкция по вводу кода финансовой разблокировки""", reply_markup=keyboard)
    await call.answer()


async def finance_order_handler(call: types.CallbackQuery):

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data=cb_finance.new(action="finance14")))

    await call.message.edit_text("""Мы постараемся исправить данную ситуацию в кратчайшие сроки. \
Информация о данной ситуации автоматически сформирована и направлена в Сервисный центр.""",
                                 reply_markup=keyboard)
    await call.answer()


async def finance_sell_department_handler(call: types.CallbackQuery):

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data=cb_finance.new(action="finance15")))

    await call.message.edit_text("""Вы можете связаться с отделом продаж компании по телефону
+7 ХХХ ХХХ ХХХХ. Время работы Пн.-Пт. с 10-00 до 19-00, Сб., Вс. выходные дни.""", reply_markup=keyboard)
    await call.answer()


def register_handlers_finance(dp: Dispatcher):
    dp.register_callback_query_handler(finance_menu_handler, cb_finance.filter(action=["finance7", "finance8",
                                                                                       "finance10", "auth20"]))

    dp.register_callback_query_handler(finance_reason_handler, cb_finance.filter(action="finance3"))

    dp.register_callback_query_handler(finance_resolve_handler, cb_finance.filter(action=["finance9", "finance4"]))

    dp.register_callback_query_handler(finance_code_handler, cb_finance.filter(action="finance2"))

    dp.register_callback_query_handler(finance_info_handler, cb_finance.filter(action="finance5"))

    dp.register_callback_query_handler(finance_order_handler, cb_finance.filter(action="finance12"))

    dp.register_callback_query_handler(finance_sell_department_handler, cb_finance.filter(action="finance13"))



