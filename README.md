# Validate your .env file locally and within a pipeline

- Check you're not missing items from your .env file
- Are you manging multipe .env files for different environments?
- Need to make sure you have all the right ones?

This script will tell you if you're missing items from your env file.

# Run

If you have an `.env.example` present in the root of your repo,
then this will be taken as the list of required environment vars. 

Otherwise, create a file named `required_envs`.

```
cp required_envs.example required
```
Fill required_envs with all of the env names your application/build requires.

## Validate your env locally

In a new shell:

```
source .env
export $(grep ^[a-zA-Z] .env | cut -d= -f1)
python3 environ-validate.py
```

## Validate env inside a pipeline

Simply commit `required_envs` as a file to your repo, then run:

`python3 environ-validate.py`

In your pipeline.

