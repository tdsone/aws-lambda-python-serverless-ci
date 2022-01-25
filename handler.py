import json


def hello(event, context):
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
    }

    ## TEST 

    return {"statusCode": 200, "body": json.dumps(body)}
