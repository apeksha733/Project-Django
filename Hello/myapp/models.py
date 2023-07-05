from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name=models.CharField(max_length=122)
    last_name=models.CharField(max_length=122)
    phone_number=models.CharField(max_length=10)
    email=models.CharField(max_length=122)
    type=models.CharField(max_length=122)
    user_input=models.TextField()

    def __str__(self):
        return self.first_name

