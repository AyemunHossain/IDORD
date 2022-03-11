from django.db import models

# Create your models here.
class LinkItem(models.Model):
    link = models.CharField(max_length=500,unique=True)
    tag = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Link Iteam"