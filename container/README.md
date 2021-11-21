## How We're Using Docker Containers

brief intro (Ritik) include teeny boi on docker container and hosting, the relationship between containers and sagemaker, how building fits into it, how pushing fits into it - should be like 4 sentences

## Build Instructions

> Skim through these instructions completely before you begin!

> This process is happening on your local machine! (Ritik) explain why in a sentence

> If there's something you don't know anything about, then take three minutes and skim an explainer article about it to help contextualize your use of the material and also to help you debug any issues you might find.

1. Install Requirements
    1. Docker - Docker will need to be on your path as well. If you're on Windows then this will require [installing WSL](https://docs.microsoft.com/en-us/windows/wsl/install), something that will likely happen automatically. WSL is super cool though and if you haven't heard of it you should definitely spend 5 minutes watching a youtube video about it. Same with Docker but you should spend 10 minutes watching a video on it.
    2. AWS Command-Line Interface (AWS CLI) - make sure this is on your path by opening a terminal and entering `aws`; you should get usage details
    3. VS Code - this development environment is strongly recommended because Adin used it and can walk you through setting it up
    4. Our Github Repo - clone this into your Senior Design workspace. All upcoming steps should take place in repo/contianer/
2. Set AWS Credentials
    1. `aws configure` - this will prompt you and you'll respond with the corresponding information you can find using the upcoming instructions 
    2. Open up the AWS SSO that you use to sign in >> AWS Account >> Command line or programmatic access >> Option 3
    3. The region should be set to `us-east-1`
    4. The format should be set to `json` 
3. Set AWS Session Token
    1. `aws configure set aws_session_token <token>`'
    2. Check instruction 2.2 for session token
4. Not sure what this is honestly (Ritik)
    1. `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 432722299252.dkr.ecr.us-east-1.amazonaws.com/sagemaker`
6. Also not sure what this is (Ritik)
    1. `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-training:1.9.1-gpu-py38-cu111-ubuntu20.04`
8. Finally build to the container host
    1. `docker build . -t 432722299252.dkr.ecr.us-east-1.amazonaws.com/sagemaker:latest`

## Push Instructions

1. Not sure how to explain this (Ritik)
    1. `docker push 432722299252.dkr.ecr.us-east-1.amazonaws.com/sagemaker:latest`
        1. currently gets error message `tag invalid: The image tag 'latest' already exists in the 'sagemaker' repository and cannot be overwritten because the repository is immutable.` (Ritik from Adin)
