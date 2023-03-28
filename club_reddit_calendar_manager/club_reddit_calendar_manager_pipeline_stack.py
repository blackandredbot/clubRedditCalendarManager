from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from constructs import Construct

from club_reddit_calendar_manager.club_reddit_calendar_manager_pipeline_stages import (
    AppStage,
)


class ClubRedditCalendarManagerStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, application_prefix: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # CI/CD Integration using CDK Pipelines
        pipeline = CodePipeline(
            self,
            "Pipeline",
            pipeline_name=f"{application_prefix}Pipeline",
            synth=ShellStep(
                "Synth",
                input=CodePipelineSource.git_hub(
                    "blackandredbot/clubRedditCalendarManager", "mainline"
                ),
                commands=[
                    "npm install -g aws-cdk",
                    "python3 -m pip install -r lambda/update_calendar_reqs.txt -t ./lambda",
                    "zip -r lambda/club_reddit_calendar_manager_layer.zip ./lambda/",
                    "python -m pip install -r requirements.txt",
                    "cdk synth",
                ],
            ),
        )

        pipeline.add_stage(AppStage(self, f"{application_prefix}AppStage"))
