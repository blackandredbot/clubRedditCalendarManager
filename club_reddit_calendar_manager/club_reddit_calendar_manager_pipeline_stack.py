from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from club_reddit_calendar_manager.club_reddit_calendar_manager_pipeline_stages import AppStage
from constructs import Construct


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
                input=CodePipelineSource.git_hub(
                    "blackandredbot/clubRedditCalendarManager", "mainline"
                ),
                commands=[
                    "npm install -g aws-cdk",
                    "python -m pip install -r requirements.txt",
                    "cdk synth",
                ],
            ),
        )

        pipeline.add_stage(AppStage(self, "ApplicationStage"))
