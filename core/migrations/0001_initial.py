# Generated by Django 2.2.4 on 2019-08-21 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='None', upload_to='')),
                ('name', models.CharField(max_length=100, verbose_name='Client name')),
                ('comment', models.TextField(verbose_name='Client says')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100, verbose_name='Project name')),
                ('description', models.TextField(verbose_name='About Project')),
                ('image', models.ImageField(default='None', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('service_name', models.CharField(max_length=100, verbose_name='Service name')),
                ('description', models.TextField(verbose_name='About Service')),
            ],
        ),
    ]
