from __future__ import annotations

import typing as t

from dependency_injector.providers import Factory
from dependency_injector.containers import DeclarativeContainer

from ..request_parsers.name import NameParser

if t.TYPE_CHECKING:
    from ..request_parsers.proto import ParserProto


class RequestParsers(DeclarativeContainer):
    name_parser: t.Callable[[], ParserProto] = Factory(NameParser).add_attributes(default_name='ANONYMOUS')
