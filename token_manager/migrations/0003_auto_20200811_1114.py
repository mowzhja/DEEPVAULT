# Generated by Django 3.0.8 on 2020-08-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_manager', '0002_auto_20200811_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validtoken',
            name='valid_token',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
