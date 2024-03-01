import os
import boto3

def create_s3_bucket(bucket_name):
    try:
        s3_client = boto3.client('s3')
        s3_client.create_bucket(Bucket=bucket_name)
    except Exception as e:
        print(f"Error creating S3 bucket: {e}")

def upload_html_to_s3(bucket_name, html_files):
    try:
        s3_resource = boto3.resource('s3')
        for html_file in html_files:
            s3_resource.meta.client.upload_file(html_file, bucket_name, os.path.basename(html_file))
    except Exception as e:
        print(f"Error uploading HTML files to S3 bucket: {e}")

def configure_static_website(bucket_name):
    try:
        s3_client = boto3.client('s3')
        s3_client.put_bucket_website(
            Bucket=bucket_name,
            WebsiteConfiguration={
                'ErrorDocument': {'Key': 'error.html'},
                'IndexDocument': {'Suffix': 'index.html'}
            }
        )
    except Exception as e:
        print(f"Error configuring S3 bucket as a static website: {e}")

def main():
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    bucket_name = 'your_bucket_name'  # Update with your bucket name
    html_files = ['file1.html', 'file2.html']  # Update with your HTML files
    create_s3_bucket(bucket_name)
    upload_html_to_s3(bucket_name, html_files)
    configure_static_website(bucket_name)

if __name__ == "__main__":
    main()
