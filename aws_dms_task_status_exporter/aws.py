from aws_dms_task_status_exporter.helper import get_conf_file
import boto3
<<<<<<< HEAD
from os import getenv


cfg = get_conf_file()
dms = boto3.client(
    "dms",
    aws_access_key_id=getenv("AWS_ACCESS_KEY", default=None),
    aws_secret_access_key=getenv("AWS_SECRET_KEY", default=None),
    region_name=getenv("AWS_REGION", default=cfg["region"]),
)


def get_status_replication_tasks():
    result = []
    response = dms.describe_replication_tasks(
        Filters=[{"Name": "replication-task-id", "Values": cfg["replication-task-id"]}]
=======
from os import environ


def get_status_replication_tasks(dms_client=None):
    conf = get_conf_file()

    if not dms_client:
        dms_client = boto3.client(
            "dms",
            aws_access_key_id=environ.get("AWS_ACCESS_KEY", default=None),
            aws_secret_access_key=environ.get("AWS_SECRET_KEY", default=None),
            region_name=environ.get("AWS_REGION", default=conf["region"]),
        )

    result = []
    response = dms_client.describe_replication_tasks(
        Filters=[{"Name": "replication-task-id", "Values": conf["replication-task-id"]}]
>>>>>>> 89d55f20c0b112c79aeaa47809ddb4fc04f69744
    )["ReplicationTasks"]

    for resp in response:
        result.append(
            {
                "replication_task_identifier": resp["ReplicationTaskIdentifier"],
                "status": resp["Status"],
            }
        )

    return result
