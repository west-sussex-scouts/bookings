from uuid import uuid4
from django.conf import settings
from django.db import models
from django.utils import timezone

from users.models import Organisation

class GUIDModel(models.Model):
    class Meta:
        abstract = True

    guid = models.UUIDField()

    def save(self, *args, **kwargs):

      if not self.guid:
        self.guid = uuid4()

      super(GUIDModel, self).save(*args, **kwargs)

class Address(GUIDModel):
    class Meta:
        verbose_name_plural = "addresses"

    al1 = models.CharField(max_length=100)
    al2 = models.CharField(max_length=100, blank=True)
    al3 = models.CharField(max_length=100, blank=True)
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=8, blank=True)


    def __str__(self):
        addr_components = [self.al1, self.al2, self.al3, self.town, self.county, self.postcode]
        return "\n".join([component for component in addr_components if component])


class Location(GUIDModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Subcamp(GUIDModel):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

class Event(GUIDModel):
    # Data
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="events_attending", blank=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=False)
    has_subcamps = models.BooleanField("Event has subcamps?", default=False, help_text="Does this event have subcamps?")

    # Metadata
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="events_created")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
