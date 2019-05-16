from uuid import uuid4
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class GUIDAbstractUser(AbstractUser):
    class Meta:
        abstract = True

    guid = models.UUIDField(primary_key=True)

    def save(self, *args, **kwargs):

      if not self.guid:
        self.guid = uuid4()

      super(GUIDAbstractUser, self).save(*args, **kwargs)

class Organisation(models.Model):
    name = models.CharField(max_length=100, blank=False)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name

class CustomUser(GUIDAbstractUser):
    has_accepted_marketing = models.BooleanField('Marketing Consent',
                                                 default=False,
                                                 help_text="Has the user consented to receive marketing information?")
    email = models.EmailField('email address', blank=False)
    phone_number = models.CharField(max_length=11, blank=True)
    date_of_birth = models.DateField('Date of Birth', null=True)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    get_full_name.short_description = "Full Name"

    def get_short_name(self):
        return self.first_name
    get_short_name.short_description = "First Name"

    def __str__(self):
        return self.username