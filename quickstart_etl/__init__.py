from dagster import (
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_package_module,
)

from . import assets
from .assets.hackernews import get_assets

defs = Definitions(assets=[*load_assets_from_package_module(assets), *get_assets()])
