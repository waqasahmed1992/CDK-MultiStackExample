from aws_cdk import (
    # Duration,
    Stack,
    CfnOutput,
    aws_ec2 as ec2,
    # aws_sqs as sqs,
)
from constructs import Construct

class VpcNetwork(Stack):
    
    def __init__(self,scope: Construct,construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # define your resource here
        
        myvpc = ec2.Vpc(
            self, 
            "myiuvpc",
            cidr="10.0.0.0/16")
            
        
        #CfnOutput=(self, "myvpcid" , value=myvpc.vpc_id, export="iu-sg")    
