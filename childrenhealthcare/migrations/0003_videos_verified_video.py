# Generated by Django 4.1.7 on 2023-04-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childrenhealthcare', '0002_videos_created_by_videos_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='verified_video',
            field=models.BooleanField(default=False),
        ),
    ]
