from django.db import models


class Newsletter(models.Model):
    """ Custom model to Newsletter. """
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return f"{self.email} subscribed on newsletter"
