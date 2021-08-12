from django.db import models

# Create your models here.
class Email_sender(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name