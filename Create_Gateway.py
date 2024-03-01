import boto3

# Replace 'your_access_key_id' and 'your_secret_access_key' with your actual AWS credentials
aws_access_key_id = 'AKIAZI2LHIMVDVXJOGPX'
aws_secret_access_key = 'DO9p5C2MQTiemIRumMjF2pNFoY50oGkxn0TPPhUQ'
aws_region = 'us-east-1'

# Replace with your API details
api_name = 'new_http'
protocol_type = 'HTTP'

# Create an API Gateway V2 client
api_gateway_client = boto3.client('apigatewayv2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

# Create API
response = api_gateway_client.create_api(
    Name=api_name,
    ProtocolType=protocol_type
)

api_id = response['ApiId']
print(f"API created with ID: {api_id}")
