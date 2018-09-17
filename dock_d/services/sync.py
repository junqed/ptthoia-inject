from __future__ import annotations

import typing as t


class SyncService:
    api_url: t.Text
    ids: t.Sequence[int]

    async def get_ids(self) -> t.Sequence[int]:
        return self.ids
