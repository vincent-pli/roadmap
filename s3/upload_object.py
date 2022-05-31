#!/bin/python
'''Sample: Upload a file to cleversafe'''

import boto3

# Create an s3 resource object, pointing to Cleversafe's public "s3" endpoint
s3 = boto3.resource('s3', endpoint_url='https://172.16.249.193', verify=False, region_name=None, aws_access_key_id='Y4qS9MLLwAHON2wzWY8D', aws_secret_access_key='er4FYTSlfLTN30gLHZZqIqFEHKH4cEHcem0zMYgP',)

# The above reads credentials from environment variables, or ~/.aws/credentials file
# Alternatively, you can provide credentials with the following kwargs:
# aws_access_key_id=access_key_id,
# aws_secret_access_key=secret_access_key,

for bucket in s3.buckets.all():
    print(bucket.name)


# Create an "object" in an existing bucket named "mybucket" under filename "test.txt"
object = s3.Object('pengli-testing', 'test.txt')

# Upload the local file
object.upload_file('/tmp/test.txt')
