from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User (based off of Django's built-in User.)
class CustomUser(AbstractUser):

    STATUS = (
        ('regular', 'regular'),
        ('pro', 'pro'),
        ('admin', 'admin')
    )

    email = models.EmailField(unique = True)
    status = models.CharField(max_length = 100, choices = STATUS, default = 'regular')
    total_score = models.IntegerField(default = 0)
    

    def __str__(self):
        return self.username