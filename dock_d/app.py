from __future__ import annotations

import typing as t
import logging
import sys

from aiohttp import web

from .containers.core import Core
from .containers.handlers import Handlers

if t.TYPE_CHECKING:
    pass


def main() -> None:
    Core.logger().addHandler(logging.StreamHandler(sys.stdout))
    Core.main_config.override({'main': {'debug': True}})
    Core.network_config.override({})

    config = Core.main_config()

    app = web.Application(debug=config['main']['debug'])

    app.add_routes([web.get('/', Handlers.name_handler()),
                    web.get('/{name}', Handlers.name_handler())])

    web.run_app(app)
