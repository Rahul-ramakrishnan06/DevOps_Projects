# <a name="_in14p91ukqlz"></a>**Automating Docker Image Upload to AWS ECR using GitHub Actions**
## <a name="_ge2r88t2qdu3"></a>**Overview**
This repository provides a GitHub Actions workflow to automate the process of building a Docker image and uploading it to Amazon Elastic Container Registry (ECR). By leveraging GitHub Actions, this workflow simplifies and streamlines the deployment of Docker containers to AWS ECR.
## <a name="_k3d95evwt4sk"></a>**Prerequisites**
Before using this workflow, ensure the following prerequisites are met:

AWS Credentials:

Create an IAM user in your AWS account with the necessary permissions to push images to ECR.

Generate AWS access and secret keys for the IAM user.

GitHub Repository:

Create new private repository to your GitHub account.

Secrets in GitHub Repository:

Add the following secrets to your GitHub repository settings:

AWS\_ACCESS\_KEY\_ID: AWS access key for the IAM user.

AWS\_SECRET\_ACCESS\_KEY: AWS secret key for the IAM user.

Create a Sample Python application 

**Docker file**

- Create a docker file for the python application
- Push the Docker file to the same github repository

**Amazon ECR**
- **
  ` `Create a new ECR private repository with image scanning in your AWS account.
- ` `Create ECR resource policy to share the repository with other AWS account.


## <a name="_d8qz4uah92xa"></a>**Workflow Configuration**
The workflow is defined in the .github/workflows/main.yml file. It consists of the following steps:

Checkout Code:

Checks out the latest version of the code in the workflow.

Build Docker Image:

Uses the Docker build command to build the Docker image from the provided Dockerfile.

Login to AWS ECR:

Logs in to AWS ECR using the provided AWS credentials.

Tag Docker Image:

Tags the Docker image with the ECR repository URL.

Push Docker Image to ECR:

Pushes the tagged Docker image to the specified ECR repository.
## <a name="_536gzuivtq44"></a>**Usage**
To use this workflow, follow these steps:

- Add the necessary secrets to your GitHub repository settings.
- Trigger a GitHub Actions workflow run, either by pushing a new commit or manually triggering the workflow from the Actions tab in your GitHub repository.
- Monitor the progress of the workflow in the Actions tab. Check the workflow logs for any errors or issues.
- Once the workflow completes successfully, your Docker image should be available in the specified AWS ECR repository.
