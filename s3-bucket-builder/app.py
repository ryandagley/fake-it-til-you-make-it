#!/usr/bin/env python3
import os
#from dotenv import load_dotenv

# load the env file
#print('Loading env file')
#load_dotenv()

import aws_cdk as cdk

from s3_bucket_builder.s3_bucket_builder_stack import S3BucketBuilderStack

print ("Creating environment")
cdk_env = cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))

app = cdk.App()
S3BucketBuilderStack(app, "S3BucketBuilderStack", env=cdk_env
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

# synthesize the stack
print('Sythesizing stack')
app.synth()
