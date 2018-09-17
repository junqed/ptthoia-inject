from __future__ import annotations

import typing as t

from aiohttp import web

if t.TYPE_CHECKING:
    from logging import Logger
    from ..request_parsers.proto import ParserProto
    from ..services.proto import SyncProto


def name_handler(parser: ParserProto,
                 logger: Logger,
                 sync_service: SyncProto) -> t.Callable[[web.Request], t.Awaitable[web.Response]]:
    async def handle(request: web.Request) -> web.Response:
        name = await parser.parse(request)

        text = "Hello, " + name

        logger.debug(text)
        logger.debug(await sync_service.get_ids())

        return web.Response(text=text)

    return handle
