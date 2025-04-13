from django.db import models
from cloudinary.models import CloudinaryField


class Occasion(models.Model):
    """ Custom model for occasions: wedding, baby shower, etc. """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name



class Size(models.Model):
    """ Custom model for sizes: small, medium, large, etc. """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Gift(models.Model):
    """ Custom model for gifts. """
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    occasion = models.ForeignKey(Occasion, on_delete=models.CASCADE, related_name="gifts_by_occasion")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="gifts_by_category")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="gifts_by_size")
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    image = CloudinaryField("image", default="placeholder", null=False, blank=False)

    def __str__(self):
        return f"{self.category.name}: {self.name}"