import json
from src.predict import Lamb
import boto3
import os

'''
filename1 = '00280532F4625A5B21B74B29A47C010D9629F875'
filename2 = '0014D73E9987A3FC3DA1055D912286B95929DC6D'
filename3 = 'soft.zip'
'''

'''
#역할부여 해야함.
def s3_download_file():
    s3 = boto3.client('s3')
    bucket_name = 'pre-upload-amoin-bucket'

    response = s3.list_objects_v2(Bucket=bucket_name)

    for obj in response['Contents']:
        file_key = obj['Key']
        download_path = f"tmp/check/" + file_key  # 파일명을 임시 경로로 지>정

        # 파일 다운로드
        s3.download_file(bucket_name, file_key, download_path)

        # 다운로드 완료 메시지
        print(f"Downloaded {file_key} to {download_path}")
    return file_key
'''



def handler(event, context):
    #file = s3_download_file()
    pred = Lamb()
    result = pred.predict(filename3)

    print(result)
    #return result


handler(1, 1)
