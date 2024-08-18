from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)

class user(models.Model):
    username=models.CharField(max_length=200)
    photo=models.CharField(max_length=500)
    contacts=models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    LOGIN = models.ForeignKey(login,default=1,on_delete=models.CASCADE)

class complaint(models.Model):
    complaint = models.CharField(max_length=200)
    c_date = models.CharField(max_length=200)
    USER = models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    reply = models.CharField(max_length=200)
    r_date = models.CharField(max_length=200)

class feedback(models.Model):
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

class files(models.Model):
    blocknumber = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

class Request(models.Model):
    FILES = models.ForeignKey(files, default=1, on_delete=models.CASCADE)
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

class hashvalue(models.Model):
    hashvalue=models.TextField()
    LOGIN = models.ForeignKey(login, default=1, on_delete=models.CASCADE)


class filetype(models.Model):
    type=models.CharField(max_length=200)
    blocknumber=models.CharField(max_length=200)



