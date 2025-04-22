from django.db import models
from django.contrib.auth.models import User
from gifts.models import Gift


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'gift')

    def __str__(self):
        return f"{self.user.username} favorited {self.gift.name}"

