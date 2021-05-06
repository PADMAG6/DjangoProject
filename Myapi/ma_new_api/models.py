from django.db import models

class Admin(models.Model):
    advisor_name= models.CharField(max_length=20)
    advisor_photo_url= models.URLField(max_length=20)

    def __str__(self):
        return self.advisor_name

class User(models.Model):
    name=models.CharField(max_length=20)
    email_id = models.EmailField(max_length=30)
    password= models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Book_calls(models.Model):
    advisor_name = models.CharField(max_length=20)
    advisor_profie_pic = models.URLField(max_length=20)
    advisor_id = models.IntegerField(auto_created=True)
    book_time = models.TimeField(auto_created=True)
    book_id = models.IntegerField(auto_created=True)

    def __str__(self):
        return self.advisor_name
# Create your models here.
