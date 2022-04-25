import boto3
from flask import *
app=Flask(__name__)

def home():
    # return "Hello EC2 "
    return render_template('index.html')