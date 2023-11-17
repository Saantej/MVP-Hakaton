from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    default_acl = 'public-read'
    bucket_name = settings.MEDIA_BUCKET_NAME


class StaticStorage(S3Boto3Storage):
    default_acl = 'public-read'
    bucket_name = settings.STATIC_BUCKET_NAME
