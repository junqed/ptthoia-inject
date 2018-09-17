from __future__ import annotations

import typing as t

from aiohttp import web

from .containers.core import Core
from .containers.handlers import Handlers

if t.TYPE_CHECKING:
    pass


def main() -> None:
    Core.main_config.override({'debug': True})
    Core.network_config.override({})

    main_config = Core.main_config()
    app = web.Application(debug=main_config['debug'])

    app.add_routes([web.get('/', Handlers.name_handler()),
                    web.get('/{name}', Handlers.name_handler())])

    web.run_app(app)
