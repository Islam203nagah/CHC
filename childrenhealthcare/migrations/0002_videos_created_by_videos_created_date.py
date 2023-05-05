# Generated by Django 4.1.7 on 2023-04-27 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('childrenhealthcare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='childrenhealthcare.userdata', verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='videos',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date'),
        ),
    ]
