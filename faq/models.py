from django.db import models


# Create your models here.
class FAQ(models.Model):
    question = models.CharField(null=False, blank=False, max_length=255)
    answer = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.question
