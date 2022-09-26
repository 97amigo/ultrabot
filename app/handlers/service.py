from aiogram import Dispatcher, types
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

cb_service = CallbackData("fabnum", "action")


class Service(StatesGroup):
    service_maintain_state1 = State()
    service_repair_state1 = State()
    service_state2 = State()
    service_state2_1 = State()
    service_state3 = State()
    service_state3_1 = State()
    service_state4 = State()
    service_state5 = State()


async def service_maintain_handler(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Создать заявку", callback_data=cb_service.new(action="service2")))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_service.new(action="service1")))

    await call.message.edit_text("""Для составления заявки на техническое обслуживание оборудования нам \
потребуется некоторая информация. Нам нужно знать наработку аппарата и манипулы.""", reply_markup=keyboard)
    await Service.service_maintain_state1.set()
    await call.answer()


async def service_repair_handler(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Создать заявку", callback_data=cb_service.new(action="service4")))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_service.new(action="service3")))

    await call.message.edit_text("""Для составления заявки на ремонт оборудование нам потребуется некоторая \
информация. Нам нужно знать наработку аппарата и манипулы.""", reply_markup=keyboard)
    await Service.service_repair_state1.set()
    await call.answer()


async def service_apparat_work_time_handler(call: types.CallbackQuery, state: FSMContext):
    str = await state.get_state()
    if str != "Service.service_state4":
        await state.update_data(init_state=str)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Не могу посмотреть наработку аппарата",
                                            callback_data=cb_service.new(action="service6")))
    keyboard.add(types.InlineKeyboardButton(text="Как узнать наработку аппарата?",
                                            callback_data=cb_service.new(action="service7")))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_service.new(action="service5")))

    await Service.service_state2.set()
    await call.message.edit_text("""Введите наработку аппарата в часах:""", reply_markup=keyboard)
    await call.answer()


async def service_apparat_question_handler(call: types.CallbackQuery):

    await Service.service_state2_1.set()

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_service.new(action="service8")))

    await call.message.edit_text("""Справка о том, где посмотреть наработку аппарата.""", reply_markup=keyboard)
    await call.answer()


async def service_manipula_work_time_mhandler(message: types.Message, state: FSMContext):
    await state.update_data(apparat_time=message.text)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Не могу посмотреть наработку манипулы",
                                            callback_data=cb_service.new(action="service10")))
    keyboard.add(types.InlineKeyboardButton(text="Как узнать наработку манипулы?",
                                            callback_data=cb_service.new(action="service11")))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_service.new(action="service9")))

    await Service.service_state3.set()
    await message.answer("""Введите наработку манипулы в минутах:""", reply_markup=keyboard)
    
    
async def service_manipula_question_mhandler(call: types.CallbackQuery):

    await Service.service_state3_1.set()

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_service.new(action="service12")))

    await call.message.edit_text("""Справка о том, где посмотреть наработку манипулы.""", reply_markup=keyboard)
    await call.answer()


async def service_manipula_work_time_handler(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    action = callback_data["action"]
    if action == "service6":
        await state.update_data(apparat_time="нет данных")

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Не могу посмотреть наработку манипулы",
                                            callback_data=cb_service.new(action="service24")))
    keyboard.add(types.InlineKeyboardButton(text="Как узнать наработку манипулы?",
                                            callback_data=cb_service.new(action="service23")))
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_service.new(action="service25")))

    await Service.service_state3.set()
    await call.message.edit_text("""Введите наработку манипулы в минутах:""", reply_markup=keyboard)


async def service_manipula_question_handler(call: types.CallbackQuery):

    await Service.service_state3_1.set()

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data=cb_service.new(action="service22")))

    await call.message.edit_text("""Справка о том, где посмотреть наработку манипулы.""", reply_markup=keyboard)
    await call.answer()


async def service_check_mhandler(message: types.Message, state: FSMContext):
    await state.update_data(manipula_time=message.text)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Да", callback_data=cb_service.new(action="service14")))
    keyboard.add(types.InlineKeyboardButton(text="Изменить данные наработки",
                                            callback_data=cb_service.new(action="service15")))
    keyboard.add(types.InlineKeyboardButton(text="Сменить номер аппарата",
                                            callback_data=cb_service.new(action="service16")))
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data=cb_service.new(action="service13")))

    await Service.service_state4.set()

    user_data_local = await state.get_data()

    await message.answer(f"""Номер аппарата: {user_data_local['apparat']}
Номер манипулы: {user_data_local['manipula']}
Наработка аппарата: {user_data_local["apparat_time"]} часов
Наработка манипулы: {user_data_local["manipula_time"]} минут
Всё верно?""", reply_markup=keyboard)


async def service_check_handler(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    action = callback_data["action"]
    if action == "service10" or action == "service24":
        await state.update_data(manipula_time="нет данных")

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Да", callback_data=cb_service.new(action="service20")))
    keyboard.add(types.InlineKeyboardButton(text="Изменить данные наработки",
                                            callback_data=cb_service.new(action="service19")))
    keyboard.add(types.InlineKeyboardButton(text="Сменить номер аппарата",
                                            callback_data=cb_service.new(action="service18")))
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data=cb_service.new(action="service21")))

    await Service.service_state4.set()

    user_data_local = await state.get_data()

    await call.message.edit_text(f"""Номер аппарата: {user_data_local['apparat']}
Номер манипулы: {user_data_local['manipula']}
Наработка аппарата: {user_data_local["apparat_time"]} часов
Наработка манипулы: {user_data_local["manipula_time"]} минут
Всё верно?""", reply_markup=keyboard)


async def service_put_info_handler(call: types.CallbackQuery):
    await call.message.edit_text("""Пожалуйста, опишите кратко проблему/напишите дополнительную информацию:""")
    await Service.service_state5.set()
    await call.answer()


async def service_ok_mhandler(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Меню", callback_data=cb_service.new(action="service17")))

    await state.reset_state(with_data=False)
    await message.answer("""Спасибо за обращение. Информация о данной ситуации автоматически \
сформирована и направлена в Сервисный центр. В ближайшее время с Вами свяжется наш сотрудник.""", reply_markup=keyboard)


def register_handlers_service(dp: Dispatcher):
    dp.register_callback_query_handler(service_maintain_handler, cb_service.filter(action="auth18"))
    dp.register_callback_query_handler(service_maintain_handler, cb_service.filter(action="service5"),
                                       state=Service.service_maintain_state1)

    dp.register_callback_query_handler(service_repair_handler, cb_service.filter(action="auth19"))
    dp.register_callback_query_handler(service_repair_handler, cb_service.filter(action="service5"),
                                       state=Service.service_repair_state1)

    dp.register_callback_query_handler(service_apparat_work_time_handler, cb_service.filter(action=["service2",
                                                                                                    "service4",
                                                                                                    "service8",
                                                                                                    "service9",
                                                                                                    "service25",
                                                                                                    "service15",
                                                                                                    "service19"]),
                                       state="*")

    dp.register_callback_query_handler(service_apparat_question_handler, cb_service.filter(action="service7"),
                                       state="*")

    dp.register_message_handler(service_manipula_work_time_mhandler, state=Service.service_state2)
    dp.register_callback_query_handler(service_manipula_work_time_mhandler, cb_service.filter(action="service12"),
                                       state="*")
    dp.register_callback_query_handler(service_manipula_question_mhandler, cb_service.filter(action="service11"),
                                       state="*")

    dp.register_callback_query_handler(service_manipula_work_time_handler, cb_service.filter(action=["service6",
                                                                                             "service22"]),
                                       state="*")
    dp.register_callback_query_handler(service_manipula_question_handler, cb_service.filter(action="service23"),
                                       state="*")

    dp.register_message_handler(service_check_mhandler, state=Service.service_state3)
    dp.register_callback_query_handler(service_check_handler, cb_service.filter(action=["service10", "service24"]),
                                       state=Service.service_state3)

    dp.register_callback_query_handler(service_put_info_handler, cb_service.filter(action=["service14", "service20"]),
                                       state="*")

    dp.register_message_handler(service_ok_mhandler, state=Service.service_state5)







