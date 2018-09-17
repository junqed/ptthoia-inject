from __future__ import annotations

import typing as t

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton, Callable, Object

from ..services.sync import SyncService

if t.TYPE_CHECKING:
    from ..services.proto import SyncProto


class Services(DeclarativeContainer):
    ids = Callable(lambda: [1, 2, 3])
    api_url = Object('https://ya.ru')

    sync_service: t.Callable[[], SyncProto] = Singleton(SyncService).add_attributes(ids=ids, api_url=api_url)
