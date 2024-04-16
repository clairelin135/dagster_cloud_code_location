from dagster import (
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_package_module,
)

from . import assets

defs = Definitions(assets=[*load_assets_from_package_module(assets)])
