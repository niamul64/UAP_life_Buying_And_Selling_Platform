from django.db import models

# Create your models here.
class admin_sector(models.model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name
