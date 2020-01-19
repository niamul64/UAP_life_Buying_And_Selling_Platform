from django.db import models

# Create your models here.
class Post_Ad(models.model):
    price = models.IntegerField(max_length=50, default="")
    title = models.TextField(max_length=200, default="")
    description = models.TextField(max_length=1000, default="")
    ad_post_date = models.DateField(max_length=20, default="")

    def __str__(self):
        return self.price
        return self.title
        return self.description
        return self.ad_post_date