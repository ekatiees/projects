# AWS S3 Uploader

The AWS S3 Uploader is a command-line tool that simplifies the process of uploading files to Amazon S3 cloud storage. It makes it convenient for users of all technical levels to manage their S3 storage.

### Features
- **Effortless file upload**: Upload single files or entire directoties without any command.
- **Create new storage buckets**: Create new buckets on demand.
- **Error handling**: Receive clear errormessages ad suggestions for resolving upload issues.

## Prerequisites
1. AWS Access Key ID and AWS Secret Key
2. Right permissions for the user associated with the keys (1)\*
3. Installed AWS CLI
4. Login with **```aws configure```** command using the keys (1)

\* AmazonS3FullAccess policy provides full access to all buckets, and is enough for running AWS S3 Uploader.


## Installation
### AWS CLI
Execute **```install_awscli```** file OR copy and paste into the terminal the following:

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
### AWS S3 Uploader
No installation needed.

Grant executable permissions to the script using:
```
chmod +x awss3uploader
```

Additionally, to access the tool from anywhere add the script to $PATH variable. It can be done with the following code (or similar):
```
cp awss3uploader /usr/local/bin
```

## Usage
1. Open a terminal window and navigate to the directory containing the ```awss3uploader``` script and execute it **OR** just use command **```awss3uploader```** in the terminal if the script has been added to $PATH variable.
2. Follow the instructions in the terminal provided by the tool.

## Examples
### Create a bucket and upload a single file
```
Create a new bucket? [y/n]: y
Please, enter a bucket name: sample-bucket
Do you want to use the default region for the bucket? [y/n]: y
make_bucket: sample-bucket
Please, enter the path to the source file/directory: source-path.txt
upload: ./source-path.txt to s3://sample-bucket/source-path.txt
The files have been successfully uploaded.
```
### Choose existing bucket and upload a directory
```
Create a new bucket? [y/n]: n
Enter the name of the bucket you want to upload files to: sample-bucket
Please, enter the path to the source file/directory: /source-path
upload: ./file1.txt to s3://sample-bucket/file1.txt
upload: ./file2.txt to s3://sample-bucket/file2.txt
...
upload: ./fileN.txt to s3://sample-bucket/fileN.txt
The files have been successfully uploaded.
```
## Author
The project performed by [ekatiees](https://github.com/ekatiees).