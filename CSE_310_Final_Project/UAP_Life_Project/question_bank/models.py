from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.utils.text import slugify
from django.dispatch import receiver


def upload_location(instance, filename, *args, **kwargs):
    file_path = 'question/{author_id}/{department}-{question_type}-{session}-{filename}'.format(
        author_id=str(instance.author.id), department=str(instance.department), question_type=str(instance.question_type), session=str(instance.session), filename=filename
    )
    return file_path


class Question(models.Model):
    department = models.CharField(max_length=20, null=False, blank=False)
    question_type = models.CharField(max_length=20, null=False, blank=False)
    exam_date = models.DateField(null=False, blank=False)
    semester = models.CharField(null=False, blank=False, max_length=20)
    session = models.CharField(null=False, blank=False, max_length=20)
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='date_published')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='date_updated')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.question_type + '-' + self.department + '-' + self.semester


receiver(post_delete, sender='Question')


def submission_delete(sender, instance):
    instance.image.delete(False)


def pre_save_question_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.department + "-" + instance.question_type +
                                "-" + instance.semester + "-" + instance.session)


pre_save.connect(pre_save_question_receiver, sender=Question)
