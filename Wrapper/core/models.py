from ast import Mod
from operator import mod
from pyexpat import model
from django.db import models


class BaseInformation(models.Model):
    domain = models.CharField(max_length=500,unique=True)
    hompage = models.CharField(max_length=500,unique=True)
    signin = models.CharField(max_length=500,unique=True)
    singup = models.CharField(max_length=500,unique=True)


    class Meta:
        verbose_name = "Base Information"


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
    link = models.CharField(max_length=250,unique=True)
    page_link = models.CharField(max_length=300)
    type = models.CharField(max_length=250)
    is_auth_related = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Form Detials Iteam"



ACTION_CHOICES = ((1, "GET"), (2, "POST"), (3, "PUT"), (4, "DELETE"), (5, "PATCH"))

class Actions(models.Model):
    name = models.CharField(choices=ACTION_CHOICES, max_length=20)   



class LinkActionItem(models.Model):
    link = models.CharField(max_length=500,unique=True)
    type = models.ManyToManyField(Actions)
    
    class Meta:
        verbose_name = "Link Action Iteam"

class LinkActionItemResponse(models.Model):
    action = models.ForeignKey(LinkActionItem, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=50)

    
    class Meta:
        verbose_name = "Link Action Iteam Response"