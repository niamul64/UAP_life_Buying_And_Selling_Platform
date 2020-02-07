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

    DEPT_CHOICES = (
        ('CSE','CSE'),
        ('EEE', 'EEE'),
        ('CIVIL', 'CIVIL'),
        ('ARCHITECTURE', 'ARCHITECTURE'),
        ('PHARMACY', 'PHARMACY'),
        ('ENGLISH','ENGLISH'),
        ('BBA','BBA'),
    )

    subject = models.CharField(max_length=20,null=False,blank=False)
    department = models.CharField(max_length=20, null=False, blank=False, choices=DEPT_CHOICES)
    QUES_CHOICES = (
        ('MID', 'MID'),
        ('CT', 'CT'),
        ('FINAL', 'FINAL'),
    )
    question_type = models.CharField(max_length=20, null=False, blank=False,choices=QUES_CHOICES)
    exam_date = models.DateField(null=False, blank=False)
    SEM_CHOICES = (
        ('1.1','1.1'),
        ('1.2', '1.2'),
        ('2.1', '2.1'),
        ('3.1', '3.1'),
        ('3.2', '3.2'),
        ('4.1', '4.1'),
        ('4.4', '4.2'),
    )
    semester = models.CharField(null=False, blank=False, max_length=20,choices=SEM_CHOICES)
    SESSION_CHOICES =(
        ('SPRING', 'SPRING'),
        ('FALL', 'FALL')
    )
    session = models.CharField(null=False, blank=False, max_length=20,choices=SESSION_CHOICES)
    image1 = models.ImageField(upload_to=upload_location, null=False, blank=False)
    image2 = models.ImageField(upload_to=upload_location,null=True,blank=True)
    image3 = models.ImageField(upload_to=upload_location,null=True,blank=True)
    image4 = models.ImageField(upload_to=upload_location,null=True,blank=True)
    image5 = models.ImageField(upload_to=upload_location,null=True,blank=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='date_published')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='date_updated')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.subject + '-' + self.department + '-' + self.subject + '-' + self.question_type + '-' + self.department + '-' + self.semester


receiver(post_delete, sender='Question')


def submission_delete(sender, instance):
    instance.image.delete(False)


def pre_save_question_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + '-' + instance.subject + "-" + instance.department + "-" + instance.question_type +
                                "-" + instance.semester)


pre_save.connect(pre_save_question_receiver, sender=Question)


class Answer(models.Model):
    image1 = models.ImageField(upload_to='ans_images', blank=False, null=False)
    image2 = models.ImageField(upload_to='ans_images', blank=True)
    image3 = models.ImageField(upload_to='ans_images', blank=True)
    image4 = models.ImageField(upload_to='ans_images', blank=True)
    image5 = models.ImageField(upload_to='ans_images', blank=True)
    image6 = models.ImageField(upload_to='ans_images', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "Sol-of-qs" + str(self.question.id)+"By-" + str(self.author.username)
