import json
import csv
import boto3
from src.etl import extract as ex
from src.etl import transform as tr
from src.etl.load import load_db
from src.db_handlers import db_init


def execute(event, context):
    try:
        bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        key = event["Records"][0]["s3"]["object"]["key"]
        s3_res = boto3.resource("s3")
        s3_object = s3_res.Object(bucket_name, key)
        raw = s3_object.get()["Body"].read().decode("utf-8").splitlines()
    except Exception as e:
        print(e)

    
    df = ex.extract_csv(raw)
    df = tr.transform_run(df)
    conn = db_init.init_db()
    load_db(conn, df)
    
    print(df[:2])