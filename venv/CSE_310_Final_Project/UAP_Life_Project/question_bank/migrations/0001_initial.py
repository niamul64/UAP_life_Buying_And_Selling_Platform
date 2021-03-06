# Generated by Django 2.2 on 2020-02-04 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import question_bank.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('EEE', 'EEE'), ('CIVIL', 'CIVIL'), ('ARCHITECTURE', 'ARCHITECTURE'), ('PHARMACY', 'PHARMACY'), ('ENGLISH', 'ENGLISH'), ('BBA', 'BBA')], max_length=20)),
                ('question_type', models.CharField(choices=[('MID', 'MID'), ('CT', 'CT'), ('FINAL', 'FINAL')], max_length=20)),
                ('exam_date', models.DateField()),
                ('semester', models.CharField(choices=[('1.1', '1.1'), ('1.2', '1.2'), ('2.1', '2.1'), ('3.1', '3.1'), ('3.2', '3.2'), ('4.1', '4.1'), ('4.4', '4.2')], max_length=20)),
                ('session', models.CharField(choices=[('SPRING', 'SPRING'), ('FALL', 'FALL')], max_length=20)),
                ('image1', models.ImageField(upload_to=question_bank.models.upload_location)),
                ('image2', models.ImageField(upload_to=question_bank.models.upload_location)),
                ('image3', models.ImageField(upload_to=question_bank.models.upload_location)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date_published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date_updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
