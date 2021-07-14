from django.db import models

# Create your models here.


class DidYouKnow(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
