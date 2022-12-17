from aws_cdk import (
    # Duration,
    Stack,
    CfnOutput,
    aws_ec2 as ec2,
    # aws_sqs as sqs,
)
from constructs import Construct

class SecurityGroup(Stack):
    
    def __init__(self,scope: Construct,construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # define your resource here
        mysecurity_group = ec2.SecurityGroup.from_security_group_id(self, "SG", "sg-01f63f16730b89620",
        mutable=False
        )
        #CfnOutput = (self,"mysg123",value=mysecirty_group.security_group_id,export="my-iu-sg")
