# Generated by Django 2.2 on 2020-02-07 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20200207_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='user_id',
        ),
        migrations.AddField(
            model_name='postad',
            name='cat_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.Categories'),
        ),
    ]
