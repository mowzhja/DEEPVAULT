# Generated by Django 3.0.8 on 2020-08-21 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0004_nonce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonce',
            name='nonce',
            field=models.BinaryField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='vault',
            name='app',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='vault',
            name='app_password',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='vault',
            name='app_username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
