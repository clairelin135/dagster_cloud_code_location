import base64
import json
import os
from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
import requests
from dagster import (
    AssetExecutionContext,
    MaterializeResult,
    MetadataValue,
    asset,
    HourlyPartitionsDefinition,
    BackfillPolicy,
)


@asset(
    partitions_def=HourlyPartitionsDefinition(start_date="2023-01-01-00:00"),
    backfill_policy=BackfillPolicy.single_run(),
)
def hourly_2023():
    pass


@asset(
    partitions_def=HourlyPartitionsDefinition(start_date="2021-01-01-00:00"),
    backfill_policy=BackfillPolicy.single_run(),
)
def hourly_2021():
    pass


@asset(
    partitions_def=HourlyPartitionsDefinition(start_date="2019-01-01-00:00"),
    backfill_policy=BackfillPolicy.single_run(),
)
def hourly_2019():
    pass


@asset(
    partitions_def=HourlyPartitionsDefinition(start_date="2018-01-01-00:00"),
    backfill_policy=BackfillPolicy.single_run(),
)
def hourly_2018():
    pass
