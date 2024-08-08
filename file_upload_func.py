import boto3
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def file_upload(filename,config,upload_to):
    if upload_to.lower()=='google_drive':
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)
        file = drive.CreateFile()
        file.SetContentFile(filename)
        file.Upload()

    elif upload_to.lower()=='s3':
        s3_bucket=config['s3_bucket_name']
        region=config['s3_region']
        s3 = boto3.client('s3',region=region)
        object_name = os.path.basename(filename)
        s3.upload_file(filename,s3_bucket ,object_name)

