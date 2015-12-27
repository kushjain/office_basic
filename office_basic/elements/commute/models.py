from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from elements.base.models import User, Event, Place, TimeStampedModel


class CommuteUser(User):
    """
    Proxy Model to manage users who commute
    """

    class Meta:
        proxy = True


class Vehicle(models.Model):

    license_number = models.CharField(blank=True, max_length=20,
                                      help_text=_("License number of vehicle, eg: DL 01 C AA 1111"),
                                      validators=[RegexValidator(
                                          regex=r"^[A-Z]{2}[ -][0-9]{1,2}(?: [A-Z])?(?: [A-Z]*)? [0-9]{4}$",
                                          message="Invalid License Plate Number [use capital letters only]",
                                          code="Invalid Value"
                                          )]
                                      )
    owner = models.ForeignKey(CommuteUser, help_text=_("Owner of vehicle"), related_name="vehicles",
                              on_delete=models.CASCADE)

    SCOOTER = 1
    BIKE = 2
    CAR = 3
    OTHER = 4

    TYPES = (
        (SCOOTER, "Scooter"),
        (BIKE, "Bike"),
        (CAR, "Car"),
        (OTHER, "Other Type")
    )

    type = models.PositiveSmallIntegerField(choices=TYPES, help_text=_("Own Private Vehicle Type used for commuting"),
                                            default=CAR)


class Route(TimeStampedModel):
    """
    Module for commute routes
    """

    user = models.ForeignKey(CommuteUser, related_name="routes", on_delete=models.CASCADE)
    start_location = models.ForeignKey(Place, related_name="begin_routes")
    end_location = models.ForeignKey(Place, related_name="end_routes")
    # todo : Decide on-delete behaviours

    is_primary = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Provide values for start_location and end_location here
        """

        if not self.start_location:
            self.start_location = self.user.home_location

        if not self.start_location:
            self.end_location = self.user.office_location

        super(Route, self).save(force_insert, force_update, using, update_fields)


class RouteLog(TimeStampedModel):
    """
    Contains Travel Log
    """

    route = models.ForeignKey(Route, related_name="logs", on_delete=models.CASCADE)
    date = models.DateField()
    host = models.ForeignKey(CommuteUser, related_name="managed_route_logs", on_delete=models.CASCADE)
    passengers = models.ManyToManyField(CommuteUser, related_name="passenger_route_logs")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Provide default value for host
        """

        if not self.host:
            self.host = self.route.user

        super(RouteLog, self).save(force_insert, force_update, using, update_fields)


class PickUpEvent(Event):
    """
    Records Pick-up
    """

    route = models.ForeignKey(RouteLog, related_name="pickup", on_delete=models.CASCADE)
