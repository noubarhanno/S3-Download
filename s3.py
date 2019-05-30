import boto3
import os
from datetime import datetime

s3 = boto3.resource('s3')
s3_Download = boto3.client('s3')
RootFolder = "YOUR ROOT FOLDER WHERE YOU WANT TO DOWNLOAD THE FILES TO"
f = open('PATH OF THE LOG FILE WHERE YOU WANT TO WRITE YOUR LOGS IN','a')
for bucket in s3.buckets.all():
    try:
        os.mkdir(RootFolder+bucket.name)
        RootFolderbucket = RootFolder+bucket.name+"/"
    except:
        RootFolderbucket = RootFolder+bucket.name+"/"
    for objectname in bucket.objects.all():
        RootFolderobject = RootFolderbucket
        folders = objectname.key.split('/')
        for folder in folders:
            root, ext = os.path.splitext(folder)
            if not ext:
                try:
                    os.mkdir(RootFolderobject+folder)
                    RootFolderobject = RootFolderobject + folder + "/"
                except:
                    RootFolderobject = RootFolderobject + folder + "/"
            if ext:
                s3_Download.download_file(bucket.name, objectname.key, RootFolderobject+folder)
                f.write((folder +" inside the folder "+ RootFolderobject + " has been downloded" + str(datetime.now()) + "\n")
                print(folder +" inside the folder "+ RootFolderobject + " has been downloded")
f.close()