import boto3

try:
    file=open("list.txt", "x")
    file.close()
except Exception as e:
    open("list.txt", "w").close()


#Then use the session to get the resource
s3 = boto3.resource('s3')

my_bucket = s3.Bucket('bnnb')
list = []
for my_bucket_object in my_bucket.objects.all():
   list.append(my_bucket_object.key) 
   file=open("list.txt", "a")
   file.write(my_bucket_object.key)
   file.write("\n")
   file.close()
   print(my_bucket_object.key)

print(list)