import json

def handler(event, context):
    body = event["body-json"]
    client = body["client"]
    result = f"Hello, {client}"

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }