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

    str_value = f'{str_value}\r\n{dt}'
    print(str_value)
    client.put_object(Body=str_value, Bucket='helmutcranium', Key='invocations.csv')

    qs_client = boto3.client('quicksight')
    response = qs_client.create_ingestion(DataSetId='cfea8841-af45-4c1e-8bef-2b1e0ba4ee9b',IngestionId='automatedIngestion',AwsAccountId='685263748376')
    print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World!')
    }
