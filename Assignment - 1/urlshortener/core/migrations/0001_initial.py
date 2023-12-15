# Generated by Django 5.0 on 2023-12-14 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.CharField(max_length=400)),
                ('url_id', models.CharField(max_length=5, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]