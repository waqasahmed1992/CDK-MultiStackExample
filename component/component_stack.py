from aws_cdk import (
    # Duration,
    Stack,
    CfnOutput,
    aws_s3 as s3,
    # aws_sqs as sqs,
)
from constructs import Construct

class ComponentStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        
        mybucket=s3.Bucket(
            self,
            "MyBucket",
            bucket_name="iu-aws-eu-internal-2022",
            versioned=True,
            public_read_access=True)
        CfnOutput(self,"mybucketoutputname",value=mybucket.bucket_name,export_name="glod-bucket")
        CfnOutput(self,"mybucketoutputarn",value=mybucket.bucket_arn)
        CfnOutput(self,"mybucketoutputdomain",value=mybucket.bucket_domain_name)
            
        
        anotherbucket = s3.Bucket.from_bucket_name(
            self,
            "AnotherBucket",
            bucket_name=mybucket.bucket_name)
        CfnOutput(self,"myanotherbucketoutputname",value=anotherbucket.bucket_name,export_name="myanotherbucketoutputname")
        CfnOutput(self,"myanotherbucketoutputarn",value=anotherbucket.bucket_arn)
        CfnOutput(self,"myanotherbucketoutputdomian",value=anotherbucket.bucket_domain_name)
        # example resource
        # queue = sqs.Queue(
        #     self, "ComponentQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
