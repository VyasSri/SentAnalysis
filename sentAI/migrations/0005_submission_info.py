# Generated by Django 5.0.7 on 2024-08-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentAI', '0004_analyzedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='submission_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(max_length=255)),
                ('content', models.TextField()),
                ('sentiment', models.TextField(max_length=255)),
            ],
        ),
    ]