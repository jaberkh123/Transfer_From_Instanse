import boto3

# Replace 'your_access_key_id' and 'your_secret_access_key' with your actual AWS credentials
aws_access_key_id = 'Your_Access_Key'
aws_secret_access_key = 'Your_secret'
aws_region = 'Region'

# Replace with your Lambda function details
function_name = 'lambda_API'
handler = 'lambda_API.handler'  # e.g., 'lambda_function.handler'
runtime = 'python3.9'  # or your preferred runtime

# Create a Lambda client
lambda_client = boto3.client('lambda', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

# Create Lambda function
response = lambda_client.create_function(
    FunctionName=function_name,
    Runtime=runtime,
    Role='your_lambda_execution_role_arn',  # Replace with your Lambda execution role ARN
    Handler=handler,
    Code={
        'S3Bucket': 'Your_bucket_name',
        'S3Key': 'lambda.zip'
    },
    Description='Your Lambda function description',
    Timeout=30,
    MemorySize=128
)

function_arn = response['FunctionArn']
print(f"Lambda function created with ARN: {function_arn}")
