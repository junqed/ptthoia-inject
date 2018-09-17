from __future__ import annotations

import typing as t

if t.TYPE_CHECKING:
    from aiohttp.web import Request


class NameParser:
    default_name: t.Text

    async def parse(self, request: Request) -> t.Text:
        return request.match_info.get('name', self.default_name)
