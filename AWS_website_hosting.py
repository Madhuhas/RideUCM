#!!!READ!!!
# Comment out the below code if you don't want to enable static website hosting on your bucket
# To work with below functions, you need to have the following permissions:
# s3:PutBucketWebsite
# s3:PutBucketPolicy

import boto3
import json

s3 = boto3.client('s3')

# Enable static website hosting on the bucket
def enable_static_website_hosting(bucket_name):
    website_configuration = {
        'IndexDocument': {'Suffix': 'rideucm.html'},
    }
    s3.put_bucket_website(Bucket=bucket_name, WebsiteConfiguration=website_configuration)

# Configure bucket policy to allow public read access
def configure_bucket_policy(bucket_name):
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:GetObject"],
                "Resource": f"arn:aws:s3:::{bucket_name}/*"
            }
        ]
    }
    s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(bucket_policy))

# Call the functions to enable static website hosting and configure bucket policy
enable_static_website_hosting('rideucm')
configure_bucket_policy('rideucm')

# endpoint URL
def get_website_endpoint(bucket_name):
    response = s3.get_bucket_website(Bucket=bucket_name)
    endpoint = f"http://{bucket_name}.s3-website-{response['WebsiteEndpoint']}"
    return endpoint

endpoint = get_website_endpoint('rideucm')
print(f"The endpoint URL for rideucm.html is: {endpoint}/rideucm.html")