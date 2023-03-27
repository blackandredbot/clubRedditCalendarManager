import aws_cdk as cdk
from constructs import Construct

from club_reddit_calendar_manager import ClubRedditCalendarManagerLambdaStack


class AppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambdaStack = ClubRedditCalendarManagerLambdaStack(self, "LambdaStack")
