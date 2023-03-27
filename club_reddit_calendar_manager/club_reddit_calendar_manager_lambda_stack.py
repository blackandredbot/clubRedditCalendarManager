from aws_cdk import Duration, RemovalPolicy, Stack
from aws_cdk import aws_events as events
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as _lambda
from aws_solutions_constructs.aws_eventbridge_lambda import (
    EventbridgeToLambda, EventbridgeToLambdaProps)
from constructs import Construct


class ClubRedditCalendarManagerLambdaStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        club_reddit_calendar_manager_layer = _lambda.LayerVersion(
            self,
            "ClubRedditLambdaLayer",
            removal_policy=RemovalPolicy.RETAIN,
            code=_lambda.Code.from_asset(
                "lambda/club_reddit_calendar_manager_layer.zip"
            ),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_9],
        )

        # The code that defines your stack goes here
        calendar_function = EventbridgeToLambda(
            self,
            "update_calendar",
            lambda_function_props=_lambda.FunctionProps(
                code=_lambda.Code.from_asset("lambda"),
                runtime=_lambda.Runtime.PYTHON_3_9,
                handler="update_calendar.handler",
                layers=[club_reddit_calendar_manager_layer],
                timeout=Duration.minutes(1),
            ),
            event_rule_props=events.RuleProps(
                schedule=events.Schedule.rate(Duration.hours(18))
            ),
        )

        calendar_function.lambda_function.role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMFullAccess")
        )
