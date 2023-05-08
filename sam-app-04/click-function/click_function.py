import boto3, json, os
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table_name = os.environ['TABLE_NAME']
    table = dynamodb.Table(table_name)
    print(event)
    table.put_item(
        Item={ 
            'id': '1',
            'click': json.loads(event['body'])['total']
        }
    )