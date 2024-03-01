import json

def lambda_handler(event, context):
    # Your business logic goes here
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': 'Lambda function executed successfully'}),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

    return response
