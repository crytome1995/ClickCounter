import boto3
import os
from loggers import logger


class Dynamo:
    def __init__(self, region, clicksTable, ipTable):
        os.environ["AWS_DEFAULT_REGION"] = region
        self.dynamo = boto3.client("dynamodb")
        self.clicksTable = clicksTable
        self.ipTable = ipTable

    def update_country_click_count(self, country):
        try:
            response = self.dynamo.update_item(
                TableName=self.clicksTable,
                Key={"country": {"S": country}},
                ExpressionAttributeNames={"#count": "count"},
                ExpressionAttributeValues={
                    ":increase": {
                        "N": str(1),
                    },
                    ":zero": {
                        "N": str(0),
                    },
                },
                UpdateExpression="SET #count = if_not_exists(#count, :zero) + :increase",
                ReturnValues="UPDATED_NEW",
            )
        except Exception as e:
            logger.error(
                "Failed to insert click for country {} due to: {}".format(
                    country, str(e)
                )
            )
            return False
        logger.info("Added click for country {}".format(country))
        return True

    def insert_country_ip(self, country, ip):
        try:
            response = self.dynamo.put_item(
                TableName=self.ipTable,
                Item={"ip": {"S": ip}, "country": {"S": country}},
            )
        except Exception as e:
            logger.error(
                "Failed to insert click for country {} with ip {} due to: {}".format(
                    country, ip, str(e)
                )
            )
            return False
        logger.info("Added click for country {} with ip {}".format(country, ip))
        return True
