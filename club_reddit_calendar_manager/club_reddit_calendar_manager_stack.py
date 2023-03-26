from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep


class ClubRedditCalendarManagerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # CI/CD Integration using CDK Pipelines
        pipeline = CodePipeline(
            self,
            "Pipeline",
            pipeline_name="CalendarManager",
            synth=ShellStep(
                "Synth",
                input=CodePipelineSource.git_hub("blackandredbot/clubRedditCalendarManager", "mainline"),
                commands=[
                    "npm install -g aws-cdk",
                    "python -m pip install -r requirements.txt",
                    "cdk synth",
                ],
            ),
        )

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "ClubRedditCalendarManagerQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
