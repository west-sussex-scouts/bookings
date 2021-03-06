# Generated by Django 2.0.13 on 2019-05-16 19:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField()),
                ('al1', models.CharField(max_length=100)),
                ('al2', models.CharField(blank=True, max_length=100)),
                ('al3', models.CharField(blank=True, max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('county', models.CharField(blank=True, max_length=100)),
                ('postcode', models.CharField(blank=True, max_length=8)),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('has_subcamps', models.BooleanField(default=False, help_text='Does this event have subcamps?', verbose_name='Event has subcamps?')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subcamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField()),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
