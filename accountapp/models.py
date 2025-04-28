from django.db import models
from django.db.models import CharField


# Create your models here.

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.text