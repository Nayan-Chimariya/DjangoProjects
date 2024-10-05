from django.db import models

class Post(models.Model):
    topic = models.TextField(max_length=20)
    text = models.TextField()

    def __str__(self) -> str:
        return self.topic