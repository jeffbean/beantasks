from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class BeanUser(models.Model):
    user = models.OneToOneField(User)
    user_image = models.ImageField(null=True, blank=True, upload_to='accounts/avatars/', help_text="")

    def __unicode__(self):
        return self.user.username

# def create_beanuser_callback(sender, instance, **kwargs):
#    beanuser, new = BeanUser.objects.get_or_create(user=instance)
# post_save.connect(create_beanuser_callback, User)
