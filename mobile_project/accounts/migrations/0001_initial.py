# Generated by Django 4.1.3 on 2022-11-19 17:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('standard', models.CharField(blank=True, max_length=3, null=True)),
                ('score', models.IntegerField(default=16)),
                ('first_login', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'User',
            },
        ),
        migrations.CreateModel(
            name='PhoneOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
                ('otp', models.CharField(blank=True, max_length=9, null=True)),
                ('count', models.IntegerField(default=0, help_text='Number of otp sent')),
                ('logged', models.BooleanField(default=False, help_text='If otp verification got successful')),
                ('forgot', models.BooleanField(default=False, help_text='only true for forgot password')),
                ('forgot_logged', models.BooleanField(default=False, help_text='Only true if validdate otp forgot get successful')),
            ],
            options={
                'verbose_name_plural': 'Phone',
            },
        ),
    ]
