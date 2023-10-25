from aws_cdk import (
    Stack,
    aws_s3
)
from constructs import Construct

class S3BucketBuilderStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        aws_s3.Bucket(
            self,
            '<string identifier>',
            bucket_name = '<bucket name>'
        )
