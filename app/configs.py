from dotenv import load_dotenv
import os
import boto3
basedir = os.path.abspath(__file__)
load_dotenv(os.path.join(basedir, ".env"))

ConStr = os.environ.get("ConStr")
ImageStore = os.environ.get("ImageStore")
ImageCategory = os.environ.get("ImageCategory")
ImagePromo = os.environ.get("ImagePromo")
os.environ['AWS_ACCESS_KEY_ID'] = os.environ.get("AWS_ACCESS_KEY_ID")
os.environ['AWS_SECRET_ACCESS_KEY'] = os.environ.get("AWS_SECRET_ACCESS_KEY")
S3BucketName = os.environ.get("S3BucketName")
boto_session = boto3.session.Session()
s3_client = boto_session.client('s3')