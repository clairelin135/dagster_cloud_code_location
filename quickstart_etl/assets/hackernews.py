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
from dagster_cloud.instance import DagsterCloudAgentInstance


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
