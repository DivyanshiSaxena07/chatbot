from django.db import models

# Create your models here.
class Admin(models.Model):
      name=models.CharField(max_length=120)
      file=models.FileField()
      def __str__(self):
       return self.name
 
class AppUser(models.Model):
      username=models.CharField(max_length=120)
      userpass=models.TextField(max_length=8)
      def __str__(self):
       return self.username
    