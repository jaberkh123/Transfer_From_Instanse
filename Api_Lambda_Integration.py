import boto3

# Specify your AWS credentials and region
aws_access_key_id = ''
aws_secret_access_key = ''
region_name = ''

# Create an API Gateway client
apigateway_client = boto3.client('apigateway', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Create a REST API
api_name = 'newapi_9'
api_description = 'Nothing'

api_response = apigateway_client.create_rest_api(
    name=api_name,
    description=api_description
)
api_id = api_response['id']
root_resource_id = apigateway_client.get_resources(restApiId=api_id)['items'][0]['id']
# Create a Resource
resource_path = "users"
resource_response = apigateway_client.create_resource(
    restApiId=api_id,
    parentId=root_resource_id,
    pathPart=resource_path
)

# Extract the Resource ID
resource_id = resource_response['id']

# Create a Method (e.g., GET)
http_method = 'GET'
method_response = apigateway_client.put_method(
    restApiId=api_id,
    resourceId=resource_id,
    httpMethod=http_method,
    authorizationType='NONE'
)
lambda_function_name = 'MyLambdaFunction'

# Specify the Lambda function ARN with the action (in this case, 'invoke')
lambda_function_arn = f'arn:aws:lambda:{region_name}:{aws_access_key_id}:function:{lambda_function_name}:invoke'


# Get the Lambda function details
lambda_client = boto3.client('lambda', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
lambda_function = lambda_client.get_function(FunctionName=lambda_function_name)
lambda_function_arn = lambda_function['Configuration']['FunctionArn']
print(lambda_function_arn)
integration_response = apigateway_client.put_integration(
    restApiId=api_id,
    resourceId=resource_id,
    httpMethod=http_method,
    type='AWS_PROXY',
    integrationHttpMethod='GET',
    uri=f'arn:aws:apigateway:{region_name}:lambda:path/2015-03-31/functions/arn:aws:lambda:{region_name}:637423534890:function:MyLambdaFunction/invocations'
    
)

# Deploy the API to a stage
stage_name = 'Stage1'
deployment_response = apigateway_client.create_deployment(
    restApiId=api_id,
    stageName=stage_name
)

# Get the Invoke URL for the deployed API
invoke_url = f'https://{api_id}.execute-api.{region_name}.amazonaws.com/{stage_name}/{resource_path}'

print(f'Your API Gateway Invoke URL: {invoke_url}')
