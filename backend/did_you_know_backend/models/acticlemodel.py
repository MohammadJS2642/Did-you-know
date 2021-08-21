from django.db import models
from datetime import datetime

from django.db.models.query_utils import select_related_descend


class Articles(models.Model):
    '''
        Articles class is for save article 
        every day from wikipedia
    '''
    
    title = models.CharField(max_length=500)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=datetime.now())

    def __str__(self) -> str:
        return self.title
