# Generated by Django 3.0.8 on 2020-08-11 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('token_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValidToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_token', models.CharField(default='NoneSet', max_length=150)),
                ('corresponding_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Token',
        ),
    ]
