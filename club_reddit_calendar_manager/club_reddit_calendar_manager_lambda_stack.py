from aws_cdk import Duration, Stack
from aws_cdk import aws_events as events
from aws_cdk import aws_lambda as _lambda
from aws_solutions_constructs.aws_eventbridge_lambda import (
    EventbridgeToLambda,
    EventbridgeToLambdaProps,
)
from constructs import Construct


class ClubRedditCalendarManagerLambdaStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        EventbridgeToLambda(
            self,
            "update_calendar",
            lambda_function_props=_lambda.FunctionProps(
                code=_lambda.Code.from_asset("lambda"),
                runtime=_lambda.Runtime.PYTHON_3_9,
                handler="update_calendar.handler",
            ),
            event_rule_props=events.RuleProps(
                schedule=events.Schedule.rate(Duration.minutes(5))
            ),
        )