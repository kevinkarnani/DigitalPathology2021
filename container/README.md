# Build Instructions

1.  Set AWS credentials
2.  aws configure set aws_session_token <token>
3.  aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 432722299252.dkr.ecr.us-east-1.amazonaws.com/sagemaker
4.  aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-training:1.9.1-gpu-py38-cu111-ubuntu20.04
5.  docker build . -t 432722299252.dkr.ecr.us-east-1.amazonaws.com/sagemaker:latest

# Push Instructions

1.  docker push 432722299252.dkr.ecr.us-east-1.amazonaws.com/sagemaker:latest
