from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher import FSMContext
from aiogram.utils.deep_linking import decode_payload


class Info(StatesGroup):
    info_state1 = State()


cb_info = CallbackData("fabnum", "action")


async def info_start_cmd_handler(message: types.Message, state: FSMContext):
    await Info.info_state1.set()

    args = message.get_args()
    await state.update_data(payload=decode_payload(args))

    keyboard = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton(text="Старт", callback_data=cb_info.new(action="info3")),
        types.InlineKeyboardButton(text="Инструкции", callback_data=cb_info.new(action="info1")),
        types.InlineKeyboardButton(text="Помощь", callback_data=cb_info.new(action="info2"))
    ]
    keyboard.add(*buttons)

    await message.answer('''Здравствуйте, Вас приветствует бот Группы компаний "Ультрафиолет". \
Для начала работы Вашим оборудованием нажмите Старт. \
Для получения информации по эксплуатации оборудования нажмите Инструкции \
Если что-то непонятно нажмите Помощь.''', reply_markup=keyboard)


async def info_info_cmd_handler(message: types.Message):

    keyboard = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton(text="BLZ", callback_data=cb_info.new(action="info5")),
        types.InlineKeyboardButton(text="BLZ лицо", callback_data=cb_info.new(action="info6")),
        types.InlineKeyboardButton(text="BLN", callback_data=cb_info.new(action="info7")),
        types.InlineKeyboardButton(text="Назад", callback_data=cb_info.new(action="info4"))
    ]
    keyboard.add(*buttons)

    await message.answer('''В данном разделе собрана информация об эксплуатации оборудования. \
Пожалуйста, выберите вас интересующую модель аппарата:''', reply_markup=keyboard)


async def info_help_cmd_handler(message: types.Message):

    keyboard = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data=cb_info.new(action="info8"))
    ]
    keyboard.add(*buttons)

    await message.answer('''При помощи этого Бота Вы сможете решить некоторые ситуации, связанные с работой \
оборудования. Возможно записаться на техническое обслуживание, направить заявку на ремонт, понять, что означают \
коды ошибок, разблокировать оборудование, получить инструкцию, заказать расходные материалы и решить иные рабочие \
ситуации.Для дальнейшей работы нажмите Старт и следуйте дальнейшим инструкциям.''', reply_markup=keyboard)


async def info_start_handler(call: types.CallbackQuery):

    keyboard = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton(text="Старт", callback_data=cb_info.new(action="info3")),
        types.InlineKeyboardButton(text="Инструкции", callback_data=cb_info.new(action="info1")),
        types.InlineKeyboardButton(text="Помощь", callback_data=cb_info.new(action="info2"))
    ]
    keyboard.add(*buttons)

    await call.message.edit_text('''Здравствуйте, Вас приветствует бот Группы компаний "Ультрафиолет". \
Для начала работы Вашим оборудованием нажмите Старт. \
Для получения информации по эксплуатации оборудования нажмите Инструкции \
Если что-то непонятно нажмите Помощь.''', reply_markup=keyboard)
    await call.answer()


async def info_info_handler(call: types.CallbackQuery):

    keyboard = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton(text="BLZ", callback_data=cb_info.new(action="info5")),
        types.InlineKeyboardButton(text="BLZ лицо", callback_data=cb_info.new(action="info6")),
        types.InlineKeyboardButton(text="BLN", callback_data=cb_info.new(action="info7")),
        types.InlineKeyboardButton(text="Назад", callback_data=cb_info.new(action="info4"))
    ]
    keyboard.add(*buttons)

    await call.message.edit_text('''В данном разделе собрана информация об эксплуатации оборудования. \
Пожалуйста, выберите вас интересующую модель аппарата:''', reply_markup=keyboard)
    await call.answer()


async def info_help_handler(call: types.CallbackQuery):

    keyboard = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data=cb_info.new(action="info8"))
    ]
    keyboard.add(*buttons)

    await call.message.edit_text('''При помощи этого Бота Вы сможете решить некоторые ситуации, связанные с работой \
оборудования. Возможно записаться на техническое обслуживание, направить заявку на ремонт, понять, что означают \
коды ошибок, разблокировать оборудование, получить инструкцию, заказать расходные материалы и решить иные рабочие \
ситуации.Для дальнейшей работы нажмите Старт и следуйте дальнейшим инструкциям.''', reply_markup=keyboard)
    await call.answer()


async def info_blz_handler(call: types.CallbackQuery):

    keyboard = types.InlineKeyboardMarkup(row_width=3)
    buttons = [
        types.InlineKeyboardButton(text="Документ 1",
                                   url="""https://disk.yandex.ru/i/xN01bC_dpVkF_Q"""),
        types.InlineKeyboardButton(text="Документ 2", url="""https://disk.yandex.ru/i/xN01bC_dpVkF_Q"""),
        types.InlineKeyboardButton(text="Документ 3", url="""https://disk.yandex.ru/i/xN01bC_dpVkF_Q"""),
        types.InlineKeyboardButton(text="Назад", callback_data=cb_info.new(action="info9"))
    ]
    keyboard.add(*buttons)

    await call.message.edit_text('''В данном разделе Вы сможете получить дополнительную информацию по \
оборудованию Beautylizer Therapy Spheres''', reply_markup=keyboard)
    await call.answer()


async def info_blz_face_handler(call: types.CallbackQuery):

    keyboard = types.InlineKeyboardMarkup(row_width=3)
    buttons = [
        types.InlineKeyboardButton(text="Документ 1",
                                   url="""https://disk.yandex.ru/i/xN01bC_dpVkF_Q"""),
        types.InlineKeyboardButton(text="Документ 2", url="""https://disk.yandex.ru/i/xN01bC_dpVkF_Q"""),
        types.InlineKeyboardButton(text="Документ 3", url="""https://disk.yandex.ru/i/xN01bC_dpVkF_Q"""),
        types.InlineKeyboardButton(text="Назад", callback_data=cb_info.new(action="info10"))
    ]
    keyboard.add(*buttons)

    await call.message.edit_text('''В данном разделе Вы сможете получить дополнительную информацию по \
оборудованию Beautylizer Therapy Face''', reply_markup=keyboard)
    await call.answer()


async def info_bln_handler(call: types.CallbackQuery):

    keyboard = types.InlineKeyboardMarkup(row_width=3)
    buttons = [
        types.InlineKeyboardButton(text="Документ 1",
                                   url="""https://disk.yandex.ru/i/xN01bC_dpVkF_Q"""),
        types.InlineKeyboardButton(text="Документ 2", url="""https://disk.yandex.ru/i/xN01bC_dpVkF_Q"""),
        types.InlineKeyboardButton(text="Документ 3", url="""https://disk.yandex.ru/i/xN01bC_dpVkF_Q"""),
        types.InlineKeyboardButton(text="Назад", callback_data=cb_info.new(action="info11"))
    ]
    keyboard.add(*buttons)

    await call.message.edit_text('''В данном разделе Вы сможете получить дополнительную информацию по \
оборудованию Beautylizer Therapy Pulse''', reply_markup=keyboard)
    await call.answer()


def register_handlers_info(dp: Dispatcher):
    dp.register_message_handler(info_start_cmd_handler, commands="start", state="*")
    # dp.register_message_handler(info_help_cmd_handler, commands="help", state="*")
    # dp.register_message_handler(info_info_cmd_handler, commands="info", state="*")
    # ПОКА КОМАНДЫ НЕ БУДЕМ ПУСКАТЬ

    dp.register_callback_query_handler(info_start_handler, cb_info.filter(action=["info4", "info8", "auth1"]),
                                       state='*')
    dp.register_callback_query_handler(info_info_handler, cb_info.filter(action=["info1", "info9",
                                                                                 "info10", "info11"]), state='*')
    dp.register_callback_query_handler(info_help_handler, cb_info.filter(action="info2"), state='*')
    dp.register_callback_query_handler(info_blz_handler, cb_info.filter(action="info5"), state='*')
    dp.register_callback_query_handler(info_blz_face_handler, cb_info.filter(action="info6"), state='*')
    dp.register_callback_query_handler(info_bln_handler, cb_info.filter(action="info7"), state='*')
