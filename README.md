# .env Validator

# Validate your .env file locally and within a pipeline

- Check you're not missing items from your .env file or os environment
- Exit immediately if required settings are missing

This script will tell you if you're missing items from your env file, and crucially, what they are.

### Tip

Use this package in combination with [python-dotenv](python-dotenv) in your
project.

# Run

If you have an `.env.example` present in the root of your repo,
then this will be taken as the list of required environment vars. 

Optionally, create a file named `required_envs`.


## Validate env within your app start up

```
from env_validate import validate_env
# (Optional) use python-dotenv to load your settings
from dotenv import load_dotenv


load_dotenv(verbose=True) # optional
validate_env() # will exit if any missing envs, priting missing values
```

## Validate your env locally

In a new shell:

```
source .env
export $(grep ^[a-zA-Z] .env | cut -d= -f1)
python
from env_validate import validate_env
validate_env()
```

## Validate env inside a pipeline

In your pipeline:
```
from env_validate import validate_env
validate_env()
```

