import boto3
from botocore.client import *


def create_bucket():
    demo = boto3.resource('s3')
    name = input("Enter the name of the bucket you want to create")
    demo.create_bucket(Bucket=name, CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
    # bucket = demo.Bucket(name)
    demo.Bucket(name).Acl().put(ACL='public-read')

    filename = "HelloWorld.html"

    demo.Object(name, filename).put(Body=open(filename, 'rb'))
    print(name, " created successfully !!! ")


def del_bucket():
    demo2 = boto3.resource('s3')
    name = input("Enter the name of the bucket you want to delete")
    # bucket = demo2.Bucket(name)

    demo2.Bucket(name).objects.all().delete()
    demo2.Bucket(name).delete()


def check_bucket():
    load = boto3.client('s3')

    try:
        # Call S3 to list current buckets
        response = load.list_buckets()
        print("The available buckets are \n")
        for bucket in response['Buckets']:
            print("The available buckets are \n")
            print(bucket['Name'])
        filename = input("Enter the name of the bucket whose keys you want to see \n \t")
        for key in load.list_objects(Bucket=filename)['Contents']:
            print(filename, " contains ", key['Key'])

    except ClientError:
        print("No buckets available ")
        # while True:
        #     option = input("Press y if you want to create a new object or n if you want to exit")
        #     option = option.lower()
        #     if option == 'y':
        #         create_bucket()
        #     elif option == 'n':
        #         exit(0)
        #     else:
        #         print("Invalid option selected")
        #         exit(0)


while True:
    print("\t \t \tEnter your choice \n"
          "\t \t1. Create a new bucket \n\t \t2. Delete a bucket \n\t \t3. Check if Bucket is available \n\t \t4. Exit "
          "\n \t")

    choice = int(input())

    if choice == 1:
        create_bucket()
    elif choice == 2:
        check_bucket()
        del_bucket()

    elif choice == 3:
        check_bucket()

    elif choice == 4:
        exit(0)
    else:
        print("Invalid Input")
        exit(1)

