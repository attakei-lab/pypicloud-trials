#!/usr/bin/env python
import base64

import boto3
import docker
from ansible.module_utils.basic import AnsibleModule


DOCUMENTATION = ""
EXAMPLES = ""
RETURN = ""


def run_module():
    module_args = {
        "name": {"type": "str", "required": True},
        "region": {"type": "str", "required": True},
        "aws_access_key": {"type": "str", "required": True},
        "aws_secret_key": {"type": "str", "required": True},
    }
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    result = {
        "changed": False,
        "oriignal_message": "",
        "message": "",
    }

    if module.check_mode:
        module.exit_json(**result)

    # Auth
    ecr = boto3.client(
        "ecr",
        region_name=module.params["region"],
        aws_access_key_id=module.params["aws_access_key"],
        aws_secret_access_key=module.params["aws_secret_key"],
    )
    ecr_rslt = ecr.get_authorization_token()
    auth_data = ecr_rslt["authorizationData"][0]
    user, passwd = base64.standard_b64decode(
        auth_data["authorizationToken"]
    ).decode().split(":")
    # Push
    docker_client = docker.DockerClient()
    docker_client.login(
        username=user,
        password=passwd,
        registry=auth_data["proxyEndpoint"],
    )
    docker_client.images.push(module.params["name"])


    result["changed"] = True
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
      main()
