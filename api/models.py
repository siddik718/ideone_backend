from django.db import models
import uuid

class Text(models.Model):
    text = models.TextField()
    url = models.CharField(default=uuid.uuid4,editable=False,max_length=100)

    def __str__(self):
        return self.text[:50]
