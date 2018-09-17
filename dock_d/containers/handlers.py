from __future__ import annotations

import typing as t

from dependency_injector.providers import Singleton
from dependency_injector.containers import DeclarativeContainer

from .core import Core
from .request_parsers import RequestParsers
from .services import Services
from ..handlers.name import name_handler

if t.TYPE_CHECKING:
    pass


class Handlers(DeclarativeContainer):
    name_handler: t.Callable = Singleton(
        name_handler,
        parser=RequestParsers.name_parser,
        logger=Core.logger.add_kwargs(name="name_handler"),
        sync_service=Services.sync_service
    )
