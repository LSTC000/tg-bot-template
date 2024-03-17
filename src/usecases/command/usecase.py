from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src import states
from src.common.state import StateManager
from src.config import settings
from src.keyboards import KeyboardRepository
from src.services import ServiceRepository

from ..core import CoreUseCase


class CommandUseCase(CoreUseCase):
    services: ServiceRepository = ServiceRepository()
    keyboards: KeyboardRepository = KeyboardRepository()

    _cmd_start_msg: str = settings.message.command.START

    async def start(self, message: Message, state: FSMContext) -> None:
        await StateManager.clear(state)

        await message.answer(
            text=self._cmd_start_msg,
            reply_markup=self.keyboards.inline.command.start(),
        )

        await StateManager.set_state(
            state=state, next_state=states.CommandStatesGroup.start
        )
