from django.db import models


class signup_info(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.TextField()

