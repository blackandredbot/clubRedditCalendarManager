#!/usr/bin/env python3
import os

import aws_cdk as cdk

from club_reddit_calendar_manager.club_reddit_calendar_manager_pipeline_stack import (
    ClubRedditCalendarManagerStack,
)

app = cdk.App()
default_env = cdk.Environment(account="363951782376", region="us-east-1")
application_prefix = "ClubRedditCalendarManager"

ClubRedditCalendarManagerStack(
    app,
    f"{application_prefix}Stack",
    env=default_env,
    application_prefix=application_prefix
)

app.synth()
