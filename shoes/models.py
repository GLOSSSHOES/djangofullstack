import uuid
from django.db import models
from django.urls import reverse


class Shoe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # new
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    image = models.ImageField(upload_to="shoes/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shoe_detail", args=[str(self.pk)])
