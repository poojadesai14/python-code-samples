# import boto3
# from botocore import UNSIGNED
# from botocore.client import Config
#
# s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
# response = s3.list_objects(Bucket='coderbytechallengesandbox')
# for content in response['Contents']:
#     obj_dict = s3.get_object(Bucket='coderbytechallengesandbox', Key=content['Key'])
# print(content['Key'], obj_dict['LastModified'])


import boto3

from botocore.handlers import disable_signing

s3 = boto3.resource('s3')
s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
bucket = s3.Bucket('coderbytechallengesandbox')
for obj in bucket.objects.all():
    if obj.key.startswith('__cb__'):
        print(obj.key)

# import boto3
#
# from botocore.handlers import disable_signing
#
# s3 = boto3.resource('s3')
# s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
# bucket = s3.Bucket('coderbytechallengesandbox')
# for obj in bucket.objects.all():
#     if obj.key.startswith(' __cb__'):
#         print(obj.key)
