from django.db import models

# models
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to='user_img/', null=True)

class Products(models.Model):
    img=models.ImageField(upload_to='media')
    p_name=models.CharField(max_length=50)
    p_id=models.CharField(max_length=50)
    p_price=models.IntegerField()

class User_logged(models.Model):
    pswd=models.CharField(max_length=50)

