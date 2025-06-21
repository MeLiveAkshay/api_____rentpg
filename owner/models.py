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



class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    total_room = models.IntegerField()
    pg_name = models.CharField(max_length=100)
    pg_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    pg_image_url = models.URLField(blank=True, null=True)
    facility = models.TextField()
    amenity = models.TextField()
    room_type = models.CharField(max_length=50)  # e.g., "Single", "Shared"
    is_available = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes')

    def __str__(self):
        return f"{self.pg_name} - {self.room_type}"