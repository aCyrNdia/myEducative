import os
import uuid
import awsgi

import boto3
from boto3.dynamodb.conditions import Key

from flask import request, jsonify
from flask_lambda import FlaskLambda

from website import create_app
app = create_app()

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"application/json"})
