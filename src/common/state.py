from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State

from src import schemas


class StateManager:
    @staticmethod
    async def clear(state: FSMContext) -> None:
        await state.clear()

    @staticmethod
    async def clear_state(state: FSMContext) -> None:
        await state.set_state(state=None)

    @staticmethod
    async def clear_data(state: FSMContext) -> None:
        await state.set_data({})

    @staticmethod
    async def set_state(state: FSMContext, next_state: State) -> None:
        await state.set_state(state=next_state)

    @staticmethod
    async def set_data(state: FSMContext, data: schemas.StateData) -> None:
        await state.set_data(data=data.model_dump())

    @staticmethod
    async def update_data(state: FSMContext, data: schemas.StateData) -> None:
        await state.update_data(data=data.model_dump())

    @staticmethod
    async def get_data(state: FSMContext) -> schemas.StateData:
        return schemas.StateData(**await state.get_data())
