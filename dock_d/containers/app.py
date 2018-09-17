from __future__ import annotations

import typing as t

from dependency_injector.providers import Callable
from dependency_injector.containers import DeclarativeContainer

from ..app import main

if t.TYPE_CHECKING:
    pass


class App(DeclarativeContainer):
    main = Callable(main)
