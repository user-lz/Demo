# Generated by Django 2.1.7 on 2019-06-16 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0007_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.RemoveField(
            model_name='user',
            name='c_time',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
    ]
