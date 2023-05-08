import boto3, json, os, re
dynamodb = boto3.resource('dynamodb')
sns = boto3.resource('sns')

def user_topic_arn(user_name):
    print(user_name)
    topics = sns.meta.client.list_topics()["Topics"]
    topic_arns = [topic['TopicArn'] for topic in topics]
    user_topic_arn = list(filter(lambda topic_arn: re.match(r"arn:aws:sns:eu-west-1:587338539633:"+ user_name + r"-sam-app-.*",topic_arn), topic_arns))[0]
    print('TopicArn:', user_topic_arn)
    return user_topic_arn  

def lambda_handler(event, context):
    table_name = os.environ['TABLE_NAME']
    table = dynamodb.Table(table_name)
    print(event)
    table.put_item(
      Item={ 
        'id': '1',
        'name': json.loads(event['body'])['name'],
        'feedback': json.loads(event['body'])['feedback']
      }
    )
    user_name = re.search('(.*)-sam-app.*', context.function_name).group(1)
    sns.meta.client.publish(
      TopicArn = user_topic_arn(user_name),
      Message = 'Thank you ' + json.loads(event['body'])['name'] + ' for your feedback!'
    )


print()