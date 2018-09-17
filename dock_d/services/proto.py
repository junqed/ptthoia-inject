from __future__ import annotations

import typing as t

if t.TYPE_CHECKING:
    from typing_extensions import Protocol

    class SyncProto(Protocol):
        api_url: t.Text
        ids: t.Sequence[int]

        async def get_ids(self) -> t.Sequence[int]:
            ...
