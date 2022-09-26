import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand
from app.config_reader import load_config
from app.handlers.common import register_handlers_common
from app.handlers.error import register_handlers_error
from app.handlers.finance import register_handlers_finance
from app.handlers.info import register_handlers_info
from app.handlers.auth import register_handlers_auth
from app.handlers.question import register_handlers_question
from app.handlers.service import register_handlers_service

logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Старт")
    ]
    await bot.set_my_commands(commands)


async def main():
    # Настройка логирования в stdout
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    logger.info("Starting bot")

    # Парсинг файла конфигурации
    config = load_config("config/bot.ini")

    storage = MemoryStorage()

    # Объявление и инициализация объектов бота и диспетчера
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot, storage=storage)


    # Регистрация хендлеров
    register_handlers_info(dp)
    register_handlers_auth(dp)
    register_handlers_error(dp)
    register_handlers_service(dp)
    register_handlers_finance(dp)
    register_handlers_question(dp)
    register_handlers_common(dp)

    await set_commands(bot)

    # Запуск поллинга
    await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())


