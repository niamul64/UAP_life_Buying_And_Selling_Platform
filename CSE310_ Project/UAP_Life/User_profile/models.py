from django.db import models

# Create your models here.
class User_profile(models.model):
    name = models.CharField(max_length=100, default="")
    dept = models.CharField(max_length=100, default="")
    Reg_ID = models.IntegerField(max_length=100, default="")
    contact = models.TextField(max_length=100, default="")
    email = models.EmailField(max_length=50, default="")
    status =models.TextField(max_length=100, default="")

    def __str__(self):
        return self.name
        return self.dept
        return self.Reg_ID
        return self.contact
        return self.email
        return self.status