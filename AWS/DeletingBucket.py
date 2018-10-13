import boto3

demo2 = boto3.resource('s3')

bucket = demo2.Bucket('pycharmbucketabhi')
# bucket1 = demo2.Bucket('abhihelloworldhtml')
# bucket2 = demo2.Bucket('consolebucketabhishek')

bucket.objects.all().delete()
bucket.delete()

