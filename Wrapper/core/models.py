from django.db import models


class BaseInformation(models.Model):
    """
    This class contains the base information of the crawling webiste
    """
    domain      = models.CharField(max_length=500,unique=True)
    hompage     = models.CharField(max_length=500,unique=True)
    signin      = models.CharField(max_length=500,unique=True)
    singup      = models.CharField(max_length=500,unique=True)

    class Meta:
        verbose_name = "Base Information"

class LoggedInUser(models.Model):
    """
    This class contains the base information of the crawling webiste
    """
    username      = models.CharField(max_length=500,unique=True)
    user_id     = models.CharField(max_length=500,unique=True)

    class Meta:
        verbose_name = "Logged In User Information"



class LinkItem(models.Model):
    """
    This models is for link with object: link id/1, id=12 
    """
    base_link                   = models.CharField(max_length=500, blank=True, null=True)
    link                        = models.CharField(max_length=500,unique=True)
    tag                         = models.CharField(max_length=150, blank=True, null=True)
    link_location               = models.CharField(max_length=250) #like we found this link on nav bar
    link_location_method        = models.CharField(max_length=250) #like we found this link in a place where get request is calling, or post body is posting
    obj                         = models.PositiveBigIntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Link Iteam"


class FormItem(models.Model):
    base_link       = models.CharField(max_length=500, blank=True, null=True)
    link            = models.CharField(max_length=250)
    type            = models.CharField(max_length=250, blank=True, null=False)
    is_auth_related = models.BooleanField(default=False)
    tag             = models.CharField(max_length=150, blank=True, null=True)
    class Meta:
        verbose_name = "Form Iteam"


class FormDetailsItem(models.Model):
    """
    This model is for form link and it's details
    """
    link            = models.CharField(max_length=250,unique=True)
    page_link       = models.CharField(max_length=300)
    type            = models.CharField(max_length=250)
    is_auth_related = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Form Detials Iteam"



ACTION_CHOICES = ((1, "GET"), (2, "POST"), (3, "PUT"), (4, "DELETE"), (5, "PATCH"))

class Actions(models.Model):
    name            = models.CharField(choices=ACTION_CHOICES, max_length=20)   


class LinkActionItem(models.Model):
    """
    This is a model that have the trace of the link and it's action's.
    """
    link                = models.CharField(max_length=500,unique=True,)
    orginal_param       = models.TextField(blank=True, null=True)
    orginal_page        = models.TextField(blank=True, null=True)
    manupulated_param   = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Link Action Iteam"

class LinkActionItemPost(models.Model):
    """
    This is a model that have the trace of the link and it's action's.
    """
    link                = models.CharField(max_length=500,unique=True,)
    orginal_param       = models.TextField(blank=True, null=True)
    orginal_page        = models.TextField(blank=True, null=True)
    manupulated_param   = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Link Action Iteam post"


class LinkAction(models.Model):
    """
    This is a model that have the trace of the link and it's action's.
    """
    link                = models.CharField(max_length=500,unique=True)
    action_type         = models.ManyToManyField(Actions, default=1)
    is_loggedin         = models.CharField(max_length=150, blank=True, null=True)
    full_page           = models.TextField(blank=True, null=True)
    started_time        = models.DateField(auto_now_add=True)
    completed_time      = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Link Action"


class LinkActionItemResponse(models.Model):
    """
    This model is for the response of the server that we attacked.
    """
    action                   = models.TextField(blank=True, null=True)
    status                   = models.CharField(max_length=50) #success or not
    is_idor                  = models.BooleanField(default=True)
    action_link              = models.CharField(max_length=500,blank=True, null=True)
    effected_full_page       = models.TextField(blank=True, null=True)
    tag                      = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Link Action Item Response"