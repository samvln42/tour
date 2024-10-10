# Generated by Django 5.0.3 on 2024-04-24 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email Address')),
                ('nickname', models.CharField(blank=True, max_length=30, null=True, verbose_name='nickname')),
                ('profile_image', models.FileField(blank=True, null=True, upload_to='media/', verbose_name='profile image')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_owner', models.BooleanField(default=False, verbose_name='Owner')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Administrator')),
            ],
            options={
                'verbose_name_plural': '1. User information',
            },
        ),
    ]
