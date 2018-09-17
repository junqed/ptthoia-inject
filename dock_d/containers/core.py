from __future__ import annotations

import typing as t
import logging

from dependency_injector.providers import (
    Configuration,
    Factory,
)
from dependency_injector.containers import DeclarativeContainer

if t.TYPE_CHECKING:
    pass


class Core(DeclarativeContainer):
    main_config = Configuration('main')
    network_config = Configuration('network_config')

    logger = Factory(logging.Logger)\
        .add_kwargs(name="core")
