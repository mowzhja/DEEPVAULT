# Generated by Django 3.0.8 on 2020-08-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0005_auto_20200821_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vault',
            name='app',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='vault',
            name='app_username',
            field=models.CharField(default='', max_length=200),
        ),
    ]
