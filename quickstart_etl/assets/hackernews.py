import base64
import json
import os
from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
import requests
from dagster import (
    MaterializeResult,
    asset,
    HourlyPartitionsDefinition,
    BackfillPolicy,
    DailyPartitionsDefinition,
)
import pendulum


def get_dt(num_partitions):
    return pendulum.datetime(2024, 1, 2, 0, 0, 0, 0, tz="UTC").subtract(
        hours=num_partitions
    )


def get_assets():
    assets = []
    for n_interval in range(0, 175, 25):
        num_partitions = n_interval * 1000
        for asset_i in range(50):

            @asset(
                partitions_def=HourlyPartitionsDefinition(
                    start_date=get_dt(num_partitions)
                ),
                backfill_policy=BackfillPolicy.single_run(),
                group_name=f"{num_partitions}_partitions",
                key=[str(num_partitions), f"asset_{asset_i}"],
            )
            def hourly_asset() -> MaterializeResult:
                return MaterializeResult()

            assets.append(hourly_asset)

    return assets


@asset(
    partitions_def=DailyPartitionsDefinition(start_date="2023-01-01"),
    backfill_policy=BackfillPolicy.single_run(),
    group_name="with_backfill_policy",
)
def successful_daily_asset() -> MaterializeResult:
    return MaterializeResult()


@asset(
    partitions_def=DailyPartitionsDefinition(start_date="2023-01-01"),
    backfill_policy=BackfillPolicy.single_run(),
    group_name="with_backfill_policy",
)
def failing_daily_asset() -> None:
    raise Exception("This asset failed")


@asset(
    partitions_def=HourlyPartitionsDefinition(start_date="2023-01-01-00:00"),
    backfill_policy=BackfillPolicy.single_run(),
)
def hourly_2023() -> MaterializeResult:
    return MaterializeResult()


@asset(
    partitions_def=HourlyPartitionsDefinition(start_date="2021-01-01-00:00"),
    backfill_policy=BackfillPolicy.single_run(),
)
def hourly_2021() -> MaterializeResult:
    return MaterializeResult()


@asset(
    partitions_def=HourlyPartitionsDefinition(start_date="2019-01-01-00:00"),
    backfill_policy=BackfillPolicy.single_run(),
)
def hourly_2019() -> MaterializeResult:
    return MaterializeResult()


@asset(
    partitions_def=HourlyPartitionsDefinition(start_date="2018-01-01-00:00"),
    backfill_policy=BackfillPolicy.single_run(),
)
def hourly_2018() -> MaterializeResult:
    return MaterializeResult()
