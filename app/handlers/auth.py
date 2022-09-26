from aiogram import Dispatcher, types
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Auth(StatesGroup):
    auth_state1 = State()


cb_auth = CallbackData("fabnum", "action")

# Тестовые данные
global user_data
user_data = {'BLZ': {'SN00000001': ['M000001', 'M000002'], 'SN00000002': ['M000003', 'M000004'],
                     'SN00000003': ['M000005', 'M000006']}}


async def auth_apparat_handler(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    await Auth.auth_state1.set()

    global user_data
    await state.update_data(user_data)

    user_data_local = await state.get_data()

    apparat_list = list(user_data_local['BLZ'].keys())
    buttons = []
    for i in range(len(apparat_list)):
        buttons.append(types.InlineKeyboardButton(text=f"BLZ: {apparat_list[i]}",
                                                  callback_data=cb_auth.new(action=f"apparat{i}")))

    buttons.extend([
        types.InlineKeyboardButton(text="Вижу ошибку в списке оборудования",
                                   callback_data=cb_auth.new(action="auth2")),
        types.InlineKeyboardButton(text="Как посмотреть номер аппарата?", callback_data=cb_auth.new(action="auth3")),
        types.InlineKeyboardButton(text="Назад", callback_data=cb_auth.new(action="auth1"))
    ])
    keyboard.add(*buttons)

    if len(buttons) > 3:
        await call.message.edit_text("""Выберите аппарат, с которым собираетесь работать. 
У Вас в системе зарегистрировано следующее оборудование:""", reply_markup=keyboard)
    else:
        await call.message.edit_text("""В системе на Вас не зарегистрировано никакого \
оборудования.""", reply_markup=keyboard)
    await call.answer()


# ПРОПУСК РЕАЛИЗАЦИИ
async def auth_apparat_service_handler(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    buttons = [
        types.InlineKeyboardButton(text="Старт", callback_data=cb_auth.new(action="info3")),
        types.InlineKeyboardButton(text="Инструкции", callback_data=cb_auth.new(action="info1")),
        types.InlineKeyboardButton(text="Помощь", callback_data=cb_auth.new(action="info2"))
    ]
    keyboard.add(*buttons)

    await call.message.edit_text()
    await call.answer()


async def auth_apparat_error_handler(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_auth.new(action="auth5")))

    await call.message.edit_text("""Мы сожалеем, что обнаружена неточность в записях оборудования. \
Мы постараемся исправить данную ситуацию в кратчайшие сроки. Информация о данной ситуации автоматически \
сформирована и направлена в Сервисный центр. В ближайшее время с Вами свяжется наш сотрудник.\n
Вы можете связаться с Сервисным центром компании по телефону +7 ХХХ ХХХ ХХХХ. \
Время работы Пн.-Пт. с 10-00 до 19-00, Сб., Вс. выходные дни.""", reply_markup=keyboard)
    await call.answer()


async def auth_apparat_info_handler(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_auth.new(action="auth6")))

    await call.message.edit_text("""У аппаратов Beautylizer Therapy Spheres серийный номер размещен на этикетке ......
У аппаратов Beautyliner Pulse серийный номер размещен на этикетке ......""", reply_markup=keyboard)
    await call.answer()


async def auth_blz_handler(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    action = callback_data['action']

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data=cb_auth.new(action="auth7")),
        types.InlineKeyboardButton(text="Да", callback_data=cb_auth.new(action="auth8"))
    ]
    keyboard.add(*buttons)

    user_data_local = await state.get_data()
    apparat_list = list(user_data_local['BLZ'].keys())

    await state.update_data(apparat=apparat_list[int(action[7:])])

    await call.message.edit_text(f"""Вы выбрали аппарат BLZ: {apparat_list[int(action[7:])]}. 
Если все верно, то нажмите Да, если ошиблись, то нажмите Назад.""", reply_markup=keyboard)
    await call.answer()


async def auth_manipula_handler(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    user_data_local = await state.get_data()
    manipula_list = list(user_data_local['BLZ'][user_data_local['apparat']])

    buttons = []
    for i in range(len(manipula_list)):
        buttons.append(types.InlineKeyboardButton(text=manipula_list[i],
                                                  callback_data=cb_auth.new(action=f"manipula{i}")))

    buttons.extend([
        types.InlineKeyboardButton(text="Вижу ошибку в списке оборудования",
                                   callback_data=cb_auth.new(action="auth9")),
        types.InlineKeyboardButton(text="Как посмотреть номер манипулы?", callback_data=cb_auth.new(action="auth10")),
        types.InlineKeyboardButton(text="Назад", callback_data=cb_auth.new(action="auth11"))
    ])
    keyboard.add(*buttons)

    await call.message.edit_text("""Выберите манипулу, с которой собираетесь работать. 
У Вас в системе зарегистрированы следующие манипулы к выбранному аппарату:""", reply_markup=keyboard)
    await call.answer()


async def auth_manipula_error_handler(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_auth.new(action="auth12")))

    await call.message.edit_text("""Мы сожалеем, что обнаружена неточность в записях оборудования. \
Мы постараемся исправить данную ситуацию в кратчайшие сроки. Информация о данной ситуации автоматически \
сформирована и направлена в Сервисный центр. В ближайшее время с Вами свяжется наш сотрудник.\n
Вы можете связаться с Сервисным центром компании по телефону +7 ХХХ ХХХ ХХХХ. \
Время работы Пн.-Пт. с 10-00 до 19-00, Сб., Вс. выходные дни.""", reply_markup=keyboard)
    await call.answer()


async def auth_manipula_info_handler(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_auth.new(action="auth13")))

    await call.message.edit_text("""У аппаратов Beautylizer Therapy Spheres серийный номер манипулы можно узнать ... \
""", reply_markup=keyboard)
    await call.answer()


# ПРОПУСК РЕАЛИЗАЦИИ
async def auth_manipula_service_handler(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton(text="Старт", callback_data=cb_auth.new(action="info3")),
        types.InlineKeyboardButton(text="Инструкции", callback_data=cb_auth.new(action="info1")),
        types.InlineKeyboardButton(text="Помощь", callback_data=cb_auth.new(action="info2"))
    ]
    keyboard.add(*buttons)

    await call.message.edit_text()
    await call.answer()


async def auth_manipula_num_handler(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    action = callback_data['action']
    user_data_local = await state.get_data()
    manipula_list = list(user_data_local['BLZ'][user_data_local['apparat']])

    await state.update_data(manipula=manipula_list[int(action[8:])])

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(text="Назад", callback_data=cb_auth.new(action="auth15")),
        types.InlineKeyboardButton(text="Да", callback_data=cb_auth.new(action="auth16"))
    ]
    keyboard.add(*buttons)

    await call.message.edit_text(f"""Вы выбрали аппарат BLZ: {user_data_local['apparat']} \
и манипулу {manipula_list[int(action[8:])]}. Если все верно, то нажмите Да, если ошиблись, \
то нажмите Назад.""", reply_markup=keyboard)
    await call.answer()


async def auth_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state(with_data=False)

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="Уточнить коды ошибок", callback_data=cb_auth.new(action="auth17")),
        types.InlineKeyboardButton(text="Записаться на техническое обслуживание",
                                   callback_data=cb_auth.new(action="auth18")),
        types.InlineKeyboardButton(text="Создать заявку на ремонт", callback_data=cb_auth.new(action="auth19")),
        types.InlineKeyboardButton(text="Снять финансовую блокировку", callback_data=cb_auth.new(action="auth20")),
        types.InlineKeyboardButton(text="Другой вопрос", callback_data=cb_auth.new(action="auth21")),
        types.InlineKeyboardButton(text="Сменить тип/номер аппарата/номер манипулы",
                                   callback_data=cb_auth.new(action="auth22"))
    ]
    keyboard.add(*buttons)

    print(await state.get_data())

    await call.message.edit_text("Какое действие вы хотите совершить?", reply_markup=keyboard)
    await call.answer()


def register_handlers_auth(dp: Dispatcher):
    dp.register_callback_query_handler(auth_apparat_handler, cb_auth.filter(action=["info3", "auth22",
                                                                                    "auth5", "auth6", "auth7",
                                                                                    "service16", "auth11",
                                                                                    "service18"]), state='*')
    dp.register_callback_query_handler(auth_apparat_error_handler, cb_auth.filter(action="auth2"), state='*')
    dp.register_callback_query_handler(auth_apparat_info_handler, cb_auth.filter(action="auth3"), state='*')

    # Здесь ловим все 50 аппаратных action
    dp.register_callback_query_handler(auth_blz_handler, cb_auth.filter(action=[f"apparat{x}" for x in range(50)]),
                                       state='*')

    dp.register_callback_query_handler(auth_manipula_handler, cb_auth.filter(action=["auth8", "auth12",
                                                                                     "auth13", "auth15"]), state='*')
    dp.register_callback_query_handler(auth_manipula_error_handler, cb_auth.filter(action="auth9"), state='*')
    dp.register_callback_query_handler(auth_manipula_info_handler, cb_auth.filter(action="auth10"), state='*')

    # Здесь ловим все 50 манипульных action
    dp.register_callback_query_handler(auth_manipula_num_handler, cb_auth.filter(
        action=[f"manipula{x}" for x in range(50)]), state='*')

    dp.register_callback_query_handler(auth_menu_handler, cb_auth.filter(action=["auth16", "error11", "service1",
                                                                                 "error14", "error17", "error22",
                                                                                 "service3", "service17", "service13",
                                                                                 "finance1", "finance6", "finance14",
                                                                                 "finance15", "question1", "question3",
                                                                                 "question4", "service21"]), state="*")
