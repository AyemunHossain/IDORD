from operator import mod
from django.db import models

# Create your models here.
class LinkItem(models.Model):
    link = models.CharField(max_length=500,unique=True)
    tag = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Link Iteam"


class FormItem(models.Model):
    link = models.CharField(max_length=250)
    type = models.CharField(max_length=250, blank=True, null=False)
    is_auth_related = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Form Iteam"


class FormDetailsItem(models.Model):
    link = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    is_auth_related = models.BooleanField(default=False)

    input1 = models.CharField(max_length=250, blank=True, null=False)
    input2 = models.CharField(max_length=250, blank=True, null=False)
    input3 = models.CharField(max_length=250, blank=True, null=False)
    input4 = models.CharField(max_length=250, blank=True, null=False)
    input5 = models.CharField(max_length=250, blank=True, null=False)
    input6 = models.CharField(max_length=250, blank=True, null=False)
    input7 = models.CharField(max_length=250, blank=True, null=False)
    input8 = models.CharField(max_length=250, blank=True, null=False)

    class Meta:
        verbose_name = "Form Detials Iteam"



ACTION_CHOICES = ((1, "GET"), (2, "POST"), (3, "PUT"), (4, "DELETE"), (5, "PATCH"))

class Actions(models.Model):
    name = models.CharField(choices=ACTION_CHOICES)   



class LinkActionItem(models.Model):
    link = models.CharField(max_length=500,unique=True)
    type = models.ManyToManyField(Actions)
    
    class Meta:
        verbose_name = "Link Action Iteam"

class LinkActionItemResponse(models.Model):
    action = models.ForeignKey(LinkActionItem)
    status = models.CharField(max_length=50)

    
    class Meta:
        verbose_name = "Link Action Iteam Response"