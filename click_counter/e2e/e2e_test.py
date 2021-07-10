import os
import requests
from config import config
import boto3
import os

os.environ["AWS_DEFAULT_REGION"] = config.default_region
dynamo = boto3.client("dynamodb")
url = os.getenv("E2E_HOST")

test_country = "US"
test_ip = "123.123.123.123"


def _clean_table():
    try:
        response = dynamo.delete_item(
            TableName=config.click_bags_table, Key={"country": {"S": test_country}}
        )
        response = dynamo.delete_item(
            TableName=config.click_users_table,
            Key={"ip": {"S": test_ip}, "country": {"S": test_country}},
        )
    except Exception as e:
        print(str(e))
        raise


_clean_table()


def test_click_endpoint():
    headers = {"Content-Type": "application/json"}
    r = requests.post(url + "/click", json={"country": test_country, "ip": test_ip})
    status = r.status_code
    assert status == 200
