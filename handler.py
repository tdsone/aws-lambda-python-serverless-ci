import json
import pandas as pd

def hello(event, context):
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
    }

    test = pd.DataFrame([])

    return {"statusCode": 200, "body": json.dumps(body)}
