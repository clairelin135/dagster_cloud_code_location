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
