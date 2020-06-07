# Generated by Django 3.0.7 on 2020-06-07 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2020, 6, 7)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]