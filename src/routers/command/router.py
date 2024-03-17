from typing import Annotated

from aiogram import F, Router
from aiogram3_di import Depends
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src import states
from src.config import settings
from src.deps import DepsRepository
from src.usecases import UseCaseRepository


router = Router()


@router.message(CommandStart())
async def start_msg(
    message: Message,
    state: FSMContext,
    use_case: Annotated[UseCaseRepository, Depends(DepsRepository.use_case.get)],
) -> None:
    await use_case.command.start_msg(message=message, state=state)


@router.callback_query(
    StateFilter(states.CommandStatesGroup.start),
    F.data == settings.keyboard.data.command.START,
)
async def start_clb(
    callback: CallbackQuery,
    state: FSMContext,
    use_case: Annotated[UseCaseRepository, Depends(DepsRepository.use_case.get)],
) -> None:
    await use_case.command.start_clb(callback=callback, state=state)
