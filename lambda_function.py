from __future__ import print_function
import boto3
import os
import requests
from requests_aws4auth import AWS4Auth
import json

print('Loading function')

headers = {"Content-Type": "application/json"}


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    message = event['Records'][0]['Sns']['Message']
    return message
