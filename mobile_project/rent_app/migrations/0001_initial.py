# Generated by Django 3.2.12 on 2022-11-19 17:51

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resort_directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort_name', models.CharField(max_length=255)),
                ('resort_address', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Subsc_directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription', models.CharField(choices=[('Econom', 'Econom'), ('Business', 'Business')], max_length=20)),
                ('cost_subscr', models.PositiveIntegerField()),
                ('table_prices', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None), size=None)),
                ('resort_subsc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsc', to='rent_app.resort_directory')),
            ],
        ),
        migrations.CreateModel(
            name='Ski_directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ski_size', models.PositiveIntegerField()),
                ('ski_count', models.PositiveIntegerField()),
                ('ski_rent_cost', models.PositiveIntegerField()),
                ('resort_ski', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ski', to='rent_app.resort_directory')),
            ],
        ),
        migrations.CreateModel(
            name='Resort_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_phone', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
                ('resort_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='rent_app.resort_directory')),
            ],
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_subsc', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), default=list, size=None)),
                ('price', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=list, size=None)),
                ('subsc_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='rent_app.subsc_directory')),
            ],
        ),
        migrations.CreateModel(
            name='Boot_directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boots_size', models.PositiveIntegerField()),
                ('boots_count', models.PositiveIntegerField()),
                ('boots_rent_cost', models.PositiveIntegerField()),
                ('resort_boot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boot', to='rent_app.resort_directory')),
            ],
        ),
    ]
