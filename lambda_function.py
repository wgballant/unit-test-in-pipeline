from datetime import timezone
import datetime

import io
import json
import boto3
from botocore.errorfactory import ClientError

def lambda_handler(event, context):
    dt = datetime.datetime.utcnow().isoformat()

    client = boto3.client('s3')
    str_value = ""
    try:
        bytes_buffer = io.BytesIO()
        client.download_fileobj(Bucket='helmutcranium', Key='invocations.csv', Fileobj=bytes_buffer)
        byte_value = bytes_buffer.getvalue()
        str_value = byte_value.decode()
    except ClientError:
        pass

    str_value += f'\r\n{dt}'

    client.put_object(Body=str_value, Bucket='helmutcranium', Key='invocations.csv')

    print(str_value)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World!')
    }
