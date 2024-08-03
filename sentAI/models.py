from django.db import models


class signup_info(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.TextField()

class submission_info(models.Model):
    subject = models.TextField(max_length=255)
    content = models.TextField()
    sentiment = models.TextField(max_length=255)

# sentAI/models.py
class FormData(models.Model):
    subject = models.TextField(max_length=255)
    content = models.TextField()
    sentiment = models.TextField(max_length=255)

class AnalyzeData(models.Model):
    email_subject = models.TextField(max_length=255)
    email_content = models.TextField()