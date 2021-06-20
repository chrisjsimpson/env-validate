import os
import subprocess
import tempfile
from os import path
import logging

log = logging.getLogger(__name__)


def validate_env():
    if path.exists(".env.example"):
        env_example = subprocess.check_output(
            "awk -F '=' 'NF {print $1}' .env.example | grep --regexp=^[a-zA-Z]",  # noqa
            shell=True,
        )
        fp = tempfile.TemporaryFile()
        fp.write(env_example)
        fp.seek(0)
        required_envs = fp.readlines()
    else:
        required_envs = open("required_envs").readlines()

    missing = []
    found_missing = False
    for env in required_envs:
        try:
            env = env.decode("utf-8").strip()
        except AttributeError:
            env = env.strip()

        if env not in os.environ:
            found_missing = True
            missing.append(env)

    if found_missing:
        log.error(
            f"env_validate. The following env settings are missing: {missing})"
        )  # noqa: E501
        exit(-1)
