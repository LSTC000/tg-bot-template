import asyncio
import sys


sys.path = ["", ".."] + sys.path[1:]

from src.server import Server  # noqa: E402


async def main() -> None:
    await Server.run()


if __name__ == "__main__":
    asyncio.run(main())
