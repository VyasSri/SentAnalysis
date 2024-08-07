# Generated by Django 5.0.7 on 2024-07-31 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentAI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('sentiment', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='submission_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.TextField()),
            ],
        ),
    ]
