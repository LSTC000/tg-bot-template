from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src import schemas, states
from src.messages import MessageRepository
from src.common.message import MessageManager
from src.common.keyboard import KeyboardManager
from src.common.state import StateManager
from src.config import settings
from src.keyboards import KeyboardRepository
from src.services import ServiceRepository

from ..core import CoreUseCase


class CommandUseCase(CoreUseCase):
    services: ServiceRepository = ServiceRepository()
    keyboards: KeyboardRepository = KeyboardRepository()
    messages: MessageRepository = MessageRepository()

    _cmd_start_msg: str = settings.message.command.START
    _interaction_welcome_msg: str = settings.message.interaction.WELCOME

    async def start_msg(self, message: Message, state: FSMContext) -> None:
        user_id = message.from_user.id
        state_data = await StateManager.get_data(state)

        if state_data.last_inline_keyboard_message_id is not None:
            await KeyboardManager.remove_last_inline_keyboard(
                user_id=user_id,
                last_inline_keyboard_message_id=state_data.last_inline_keyboard_message_id,
            )

        await StateManager.clear(state)

        message_id = await self.messages.command.start(
            chat_id=user_id,
        )

        await StateManager.update_data(
            state=state,
            data=schemas.StateData(
                last_inline_keyboard_message_id=message_id
            ),
        )
        await StateManager.set_state(
            state=state, next_state=states.CommandStatesGroup.start
        )

    async def start_clb(self, callback: CallbackQuery, state: FSMContext) -> None:
        user_id = callback.from_user.id
        state_data = await StateManager.get_data(state)

        if state_data.last_inline_keyboard_message_id is not None:
            await KeyboardManager.remove_last_inline_keyboard(
                user_id=user_id,
                last_inline_keyboard_message_id=state_data.last_inline_keyboard_message_id,
            )
            await StateManager.update_data(
                state=state,
                data=schemas.StateData(last_inline_keyboard_message_id=None),
            )

        await MessageManager.send_message(
            chat_id=user_id,
            text=self._interaction_welcome_msg,
        )
