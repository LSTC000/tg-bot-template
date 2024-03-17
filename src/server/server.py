from .abc import ABCServer
from .bot import ServerBot
from .cache import ServerCache
from .commands import ServerCommands
from .deps import ServerDeps
from .log import ServerLog
from .routers import ServerRouters
from .storage import ServerStorage


class Server(ABCServer):
    @staticmethod
    async def run() -> None:
        ServerLog.init()
        ServerCache.init()
        dp, bot = await ServerBot.init(storage=ServerStorage.get_storage(redis=True))
        ServerRouters.init(dp=dp)
        ServerDeps.init(dp=dp)
        await ServerCommands.init(bot=bot)
        await ServerBot.run(dp=dp, bot=bot)
