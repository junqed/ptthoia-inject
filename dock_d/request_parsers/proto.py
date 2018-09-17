from __future__ import annotations

import typing as t

if t.TYPE_CHECKING:
    from aiohttp.web import Request

    import typing_extensions as te

    T = t.TypeVar('T', covariant=True)


    class ParserProto(te.Protocol[T]):
        async def parse(self, request: Request) -> T:
            ...
