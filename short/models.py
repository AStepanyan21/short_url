from django.db import models


class URL(models.Model):
    """URL database"""
    base_url = models.TextField()
    short_url = models.CharField(max_length=10)