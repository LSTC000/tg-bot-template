from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

from src.config import settings

from .abc import ABCServerCommands


class ServerCommands(ABCServerCommands):
    _cmd_start_name: str = settings.command.START.name
    _cmd_start_desc: str = settings.command.START.description

    @classmethod
    async def init(cls, bot: Bot) -> None:
        commands = [
            BotCommand(
                command=cls._cmd_start_name,
                description=cls._cmd_start_desc,
            ),
        ]

        await bot.set_my_commands(commands, BotCommandScopeDefault())
