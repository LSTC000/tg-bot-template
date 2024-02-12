from .abc import ABCDepsRepository
from .db import DatabaseDeps
from .usecase import UseCaseDeps


class DepsRepository(ABCDepsRepository):
    db: DatabaseDeps = DatabaseDeps()
    use_case: UseCaseDeps = UseCaseDeps()
