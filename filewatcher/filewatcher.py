import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # Connect to S3
    s3 = boto3.client('s3')
    
    # Connect to SNS
    sns = boto3.client('sns')
    
    # Specify your bucket name
    bucket_name = 'my-bucket-name'
    
    # Calculate the date 7 days ago
    seven_days_ago = datetime.now() - timedelta(days=7)
    
    # List objects in the bucket
    objects = s3.list_objects_v2(Bucket=bucket_name)['Contents']
    
    # Collect objects older than 7 days
    old_objects = []
    for obj in objects:
        if obj['LastModified'].replace(tzinfo=None) < seven_days_ago:
            old_objects.append(obj)
    
    # Create email content
    email_body = "List of objects older than 7 days:\n"
    for obj in old_objects:
        email_body += f"Object: {obj['Key']}, Modified Date: {obj['LastModified']}\n"
    
    # Send email using SNS
    sns.publish(
        TopicArn='my-sns-arn',
        Subject='Old Objects Report',
        Message=email_body
    )
