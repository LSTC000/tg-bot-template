from src.crud import CRUDRepository

from ..core import CoreService
from .utils import CommandServiceUtils


class CommandService(CoreService):
    utils: CommandServiceUtils = CommandServiceUtils()
    crud: CRUDRepository = CRUDRepository()
