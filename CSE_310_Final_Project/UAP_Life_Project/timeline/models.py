from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=20,null=False,blank=False)
    description = models.TextField(max_length=20)
    price = models.IntegerField(max_length=10, null=False, blank=False)
    image1 = models.ImageField(upload_to='post_pics/')
    image2 = models.ImageField(upload_to='question_bank/')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='date_published')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.department + ',' + self.question_type + ',' + self.semester + ',' + self.session




