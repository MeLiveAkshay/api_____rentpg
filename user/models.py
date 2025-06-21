from django.db import models

# Create your models here.
class UserDetails(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    user_phone = models.CharField(max_length=15)
    profession = models.CharField(max_length=100)
    address = models.TextField()
    current_address = models.TextField()

    def __str__(self):
        return self.user_name


