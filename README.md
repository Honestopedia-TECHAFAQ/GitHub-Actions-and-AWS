# My Project

This project deploys HTML files to an S3 bucket and configures it as a static website using GitHub Actions.

## Developer

- **Developer:** Afaq Ahmad

## Deployment Process

To automate the deployment process, we use GitHub Actions along with a Python script (`deploy_to_s3.py`). This script creates an S3 bucket, uploads HTML files to the bucket, and configures it as a static website.

### Python Script (`deploy_to_s3.py`)

Below is the Python script used for deployment:

```python
import os
import boto3

# Define functions for creating S3 bucket, uploading HTML files, and configuring static website

# Main function orchestrating the deployment process

if __name__ == "__main__":
    main()
