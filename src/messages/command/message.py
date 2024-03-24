from src.common.message import MessageManager
from src.config import settings
from src.keyboards import KeyboardRepository
from src.services import ServiceRepository

from ..core import CoreMessage


class CommandMessage(CoreMessage):
    services: ServiceRepository = ServiceRepository()
    keyboards: KeyboardRepository = KeyboardRepository()

    _cmd_start_msg: str = settings.message.command.START

    async def start(
        self,
        chat_id: int,
    ) -> int:
        message = await MessageManager.send_message(
            chat_id=chat_id,
            text=self._cmd_start_msg,
            reply_markup=self.keyboards.inline.command.start(),
        )
        return message.message_id
