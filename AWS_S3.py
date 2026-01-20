# Sai Madhuhas Kotini
# AWS S3 bucket creation

import boto3
import json

s3 = boto3.client('s3')

# creating S3 bucket
region = "us-east-2"
def createS3Bucket(bucket_name, location):
    "create a bucket"
    result = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    return result
bucket_name = "rideucm"
location =  {"LocationConstraint": region}
result = createS3Bucket(bucket_name, location)
print(result)

# function that will upload my static website to my newly created bucket
def upload_file(file_name, bucket_name):
    try:
        s3.upload_file(file_name, bucket_name, file_name)
        print(f'Successfully uploaded {file_name} to {bucket_name}.')
        return True
    except Exception as e:
        print(f'Error uploading {file_name} to {bucket_name}: {e}')
        return False
upload_file('index.html', 'rideucm')
upload_file('style.css', 'rideucm')
upload_file('zoom-bg-gomules.jpg', 'rideucm')

# List the content of my bucket
def list_bucket_contents(bucket_name):
    response = s3.list_objects_v2(Bucket=bucket_name)
    for obj in response['Contents']:
        print(obj['Key'])
list_bucket_contents('rideucm')

# Enable static website hosting on the bucket
def enable_static_website_hosting(bucket_name):
    website_configuration = {
        'IndexDocument': {'Suffix': 'rideucm.html'},
    }
    s3.put_bucket_website(Bucket=bucket_name, WebsiteConfiguration=website_configuration)
