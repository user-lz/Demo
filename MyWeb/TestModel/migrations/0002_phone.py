# Generated by Django 2.1.7 on 2019-04-18 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=20)),
            ],
        ),
    ]
