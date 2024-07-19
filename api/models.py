from django.db import models

# Create your models here.

class Blog(models.Model):
    body = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]