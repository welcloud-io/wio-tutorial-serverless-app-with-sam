import boto3, json, os, re
dynamodb = boto3.resource('dynamodb')
sns = boto3.resource('sns')
sts = boto3.client('sts')

region = boto3.session.Session().region_name

# ------------------------------------------------------------------------------
# Record Feedback
# ------------------------------------------------------------------------------
def record_feedback(id, name, feedback):
    table_name = os.environ['TABLE_NAME']
    table = dynamodb.Table(table_name)
    table.put_item(
      Item={ 
        'id': '1',
        'name': name,
        'feedback': feedback
      }
    )

# ------------------------------------------------------------------------------
# Confirm feedback
# ------------------------------------------------------------------------------
def topic_arn():
    account_id = sts.get_caller_identity()["Account"]
    topics = sns.meta.client.list_topics()["Topics"]
    topic_arns = [topic['TopicArn'] for topic in topics]
    topic_arn = list(
      filter(
        lambda topic_arn: re.match(r"arn:aws:sns:" + region + ":" + account_id + ":" + r"simple-sam-app-.*",topic_arn), 
        topic_arns
      )
    )[0]
    print('TopicArn:', topic_arn)
    return topic_arn 

    
def confirm_feedback(name):
    sns.meta.client.publish(
      TopicArn = topic_arn(),
      Message = 'Thank you ' + name + ' for your feedback!'
    )

# ------------------------------------------------------------------------------
# Lambda Handler 
# ------------------------------------------------------------------------------
def lambda_handler(event, context):
    record_feedback('1', json.loads(event['body'])['name'], json.loads(event['body'])['feedback'])
    confirm_feedback(json.loads(event['body'])['name'])