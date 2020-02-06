from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# custom user manager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, reg_id,password=None):
        if not email:
            raise ValueError("User must have an email !")
        if not username:
            raise ValueError("User must have a username !")
        if not first_name:
            raise ValueError("User must have a first_name !")
        if not last_name:
            raise ValueError("User must have a last_name !")
        if not reg_id:
            raise ValueError("User must have an reg_id !")

        user = self.model(
             email=self.normalize_email(email),
             username=username,
             first_name=first_name,
             last_name=last_name,
             reg_id=reg_id,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, reg_id, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            reg_id=reg_id,
            password=password,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here.


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60,unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    reg_id = models.CharField(max_length=20)
    DEPT_CHOICES = (
        ('CSE', 'CSE'),
        ('EEE', 'EEE'),
        ('CIVIL', 'CIVIL'),
        ('ARCHITECTURE', 'ARCHITECTURE'),
        ('PHARMACY', 'PHARMACY'),
        ('ENGLISH', 'ENGLISH'),
        ('BBA', 'BBA'),
    )
    department = models.CharField(max_length=20,choices=DEPT_CHOICES)
    profile_pic = models.ImageField('profile_pics/', blank=True)
    date_joined = models.DateField(verbose_name='date_joined',auto_now_add=True)
    last_login = models.DateField(verbose_name='last_login',auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # log in field
    USERNAME_FIELD = 'email'
    objects = MyAccountManager()
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'reg_id']

    def __str__(self):
        return self.email + ", " + self.username

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True




class Promo(models.Model):
    title = models.CharField(max_length=50,null=False,blank=False)
    description = models.TextField(max_length=200 , default="")
    image = models.ImageField(upload_to='promo_pic/')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='date_published')


    def __str__(self):
        return self.description