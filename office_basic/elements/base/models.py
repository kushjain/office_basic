from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.gis.db import models as geo_model
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):
    """
    Create an abstract time stamped model with created_at and updated_at columns
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Place(geo_model.Model):
    """
    Create a Place Model, which contains name and location of place
    """

    name = geo_model.CharField(max_length=20)
    coordinates = geo_model.PointField(srid=4326)
    state = geo_model.CharField(max_length=30, blank=True)
    country = geo_model.CharField(max_length=30, blank=True)

    # Created them again to avoid MRO issues
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    object = geo_model.GeoManager()

    def __str__(self):
        return self.name


class User(AbstractUser, TimeStampedModel):
    """
    User Model
    """

    MALE = 1
    FEMALE = 2
    OTHER = 3

    GENDERS = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    )

    gender = models.PositiveSmallIntegerField(choices=GENDERS)
    home_location = models.ForeignKey(Place, help_text=_("Home Location"), related_name="residents",
                                      on_delete=models.PROTECT)
    office_location = models.ForeignKey(Place, help_text=_("Office Location"), related_name="workers",
                                        on_delete=models.PROTECT)

    def email_user(self, subject, message, from_email=settings.DEFAULT_FROM_EMAIL, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Event(TimeStampedModel):
    """
    Records event and Participants
    """

    name = models.CharField(max_length=50, help_text=_("Name of Event"))
    start_time = models.DateTimeField(help_text=_("Start Time of Event"))
    end_time = models.DateTimeField(help_text=_("End Time of event"), null=True, blank=True)
    duration = models.DurationField(help_text=_("Duration of Event"), null=True, blank=True)
    host = models.ForeignKey(User, help_text=_("Event Host"), related_name="hosted_events",
                             on_delete=models.CASCADE)
    guests = models.ManyToManyField(User, help_text=_("Event Guest"), related_name="guest_events")
    venue = models.ForeignKey(Place, help_text=_("Event Venue"), related_name="events")
    # todo : decide on-delete behaviour for venue

    def __str__(self):
        return "{name} - {host} - {venue}".format(name=self.name, host=self.host.username, venue=self.venue.name)

    def clean(self):
        """
        Model Validations
        """

        if self.end_time:
            if self.end_time < self.start_time:
                raise ValidationError({'end_time': _("End time cannot be smaller than start time")})

            if self.duration:
                raise ValidationError(_("Please specify either duration or End time only"))

            self.duration = self.end_time - self.start_time

        elif self.duration:
            self.end_time = self.start_time + self.duration
