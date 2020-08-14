import os

required_envs = open('required_envs').readlines()

for env in required_envs:
    env = env.strip()
    if env not in os.environ:
       print(f"{env} not found in environment.")
       raise KeyError 
