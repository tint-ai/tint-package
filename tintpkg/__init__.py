import datarobot as dr
import pandas as pd
import boto3

name = "tintpkg"

def connect_datarobot(configFilePath='datarobot-config.yaml'):
    dr.Client(config_path=configFilePath)

def load_data_from_dr_project(project, bucket):
    com_index = project.file_name.find("com")
    key = project.file_name[com_index + 4 :]
    data_location = 's3://{}/{}'.format(bucket, key)
    data = pd.read_csv(data_location)
    return data

def load_data_from_s3_bucket(key, bucket):
    data_location = 's3://{}/{}'.format(bucket, key)
    data = pd.read_csv(data_location)
    return data

def upload_to_s3(data, bucket, key):
    from io import StringIO
    csv_buffer = StringIO()
    data.to_csv(csv_buffer)
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket, key).put(Body=csv_buffer.getvalue())
    return "Data uploaded to {}/{}".format(bucket, key)

