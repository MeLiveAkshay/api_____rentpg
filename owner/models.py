from django.db import models

class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=128)  # Suitable for hashed passwords

    def __str__(self):
        return self.name
