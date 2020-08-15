import os
import subprocess
import tempfile
from os import path

if path.exists('.env.example'):
    env_example = subprocess.check_output("awk -F '=' 'NF {print $1}' .env.example | grep --regexp=^[a-zA-Z]", shell=True)
    fp = tempfile.TemporaryFile()
    fp.write(env_example)
    fp.seek(0)
    required_envs = fp.readlines()
else:
    required_envs = open('required_envs').readlines()


for env in required_envs:
    try:
        env = env.decode('utf-8').strip()
    except AttributeError:
        env = env.strip()

    if env not in os.environ:
       print(f"{env} not found in environment.")
       raise KeyError 
