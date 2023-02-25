import os
import logging

log = logging.getLogger(__name__)


def remove_comments(lines):
    return [
        line for line in lines if line.strip() and not line.startswith("#")
    ]  # noqa: E501


def validate_env():
    env_file = os.path.join(os.getcwd(), ".env.example")
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            env_example = f.read()
        required_envs = [
            env.split("=")[0].strip()
            for env in remove_comments(env_example.split("\n"))
        ]
    else:
        with open("required_envs", "r") as f:
            required_envs = remove_comments(f.read().splitlines())

    missing = []
    found_missing = False
    for env in required_envs:
        if env not in os.environ:
            found_missing = True
            missing.append(env)

    if found_missing:
        log.error(
            f"env_validate. The following env settings are missing: {missing})"
        )  # noqa: E501
        exit(-1)
