import asyncio
import logging
import sys

from sqlalchemy.sql import text
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed


sys.path = ["", ".."] + sys.path[1:]

from src.common.logger import LoggerManager  # noqa: E402
from src.config.db import PostgresClient  # noqa: E402


logger = LoggerManager.get_base_logger()


@retry(
    stop=stop_after_attempt(60 * 5),
    wait=wait_fixed(1),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
async def init() -> None:
    db = PostgresClient.get_client()()
    try:
        response = await db.execute(text("SELECT 1"))
        logger.info(f"Response value: {response.first()}")
    except Exception as e:
        logger.error(e)
        raise e
    finally:
        await db.close()


async def main() -> None:
    logger.info("Initializing service")
    await init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    asyncio.run(main())
