from datetime import date, datetime, timedelta

from django.test import TestCase
from django.conf import settings
from django.core.exceptions import ValidationError

from django_dynamic_fixture import G
from mock import patch

from elements.base.models import Place, User, Event


class PlaceModelTest(TestCase):
    """
    Class to test Place model
    """

    @classmethod
    def setUpClass(cls):
        """
        Initial setup for test cases
        """

        cls.place = G(Place, name="test_place")
        super(PlaceModelTest, cls).setUpClass()

    def test_create(self):
        """
        Test created object
        """

        # auto id set
        self.assertIsNotNone(self.place.id)
        # Name is set
        self.assertEqual(self.place.name, "test_place")

    def test_str(self):
        """
        Test str return of object
        """

        self.assertEqual(str(self.place), "test_place")


class UserModelTest(TestCase):
    """
    Class to test User model
    """

    @classmethod
    def setUpClass(cls):
        """
        Initial setup class
        """

        cls.home = G(Place, name="home")
        cls.office = G(Place, name="office")
        cls.user = G(User, home_location=cls.home, office_location=cls.office)
        super(UserModelTest, cls).setUpClass()

    def test_create(self):
        """
        Test created object
        """

        # auto id set
        self.assertIsNotNone(self.user.id)
        # Home is set
        self.assertEqual(self.user.home_location, self.home)
        # Office is set
        self.assertEqual(self.user.office_location, self.office)

    @patch('elements.base.models.send_mail')
    def test_email_user(self, patched_send_mail):
        """
        Test Email User functionality
        """

        self.user.email_user(subject="subject", message="message")

        patched_send_mail.assert_called_with("subject", "message", settings.DEFAULT_FROM_EMAIL, [self.user.email])


class EventModelTest(TestCase):
    """
    Class to test Event model
    """

    @classmethod
    def setUpClass(cls):
        """
        Initial setup class
        """

        cls.venue = G(Place, name="venue")
        cls.host = G(User, name="host")
        super(EventModelTest, cls).setUpClass()

    def test_create(self):
        """
        Test created object
        """

        event = G(Event, name="event", venue=self.venue, host=self.host)

        # auto id set
        self.assertIsNotNone(event.id)
        # Venue is set
        self.assertEqual(event.venue, self.venue)
        # Host is set
        self.assertEqual(event.host, self.host)
        # Name is set
        self.assertEqual(event.name, "event")

    def test_str(self):
        """
        Test str return of object
        """

        event = G(Event, name="event", venue=self.venue, host=self.host, date=date.today())
        self.assertEqual(str(event), "event - {} - venue".format(self.host.username))

    def test_end_time_smaller_than_start_time(self):
        """
        Raise error if end time is smaller than start time
        """

        start_time = datetime.now()
        end_time = start_time - timedelta(seconds=10)

        event = G(Event, name="event", start_time=start_time, end_time=end_time, host=self.host, venue=self.venue)

        with self.assertRaises(ValidationError):
            event.clean()

    def test_end_time_and_duration_present(self):
        """
        Raise if both end time and duration are given
        """

        start_time = datetime.now()
        end_time = start_time + timedelta(seconds=10)

        event = G(Event, name="event", start_time=start_time, end_time=end_time, host=self.host, venue=self.venue,
                  duration=timedelta(seconds=20))

        with self.assertRaises(ValidationError):
            event.clean()

    def test_duration_set(self):
        """
        If start time and end time are give, duration is set
        """

        start_time = datetime.now()
        end_time = start_time + timedelta(seconds=10)

        event = G(Event, name="event", start_time=start_time, end_time=end_time, host=self.host, venue=self.venue,
                  duration=None)
        event.clean()
        self.assertEqual(event.duration, timedelta(seconds=10))

    def test_end_time_set(self):
        """
        If start time and duration given, end time is set
        """

        start_time = datetime.now()
        duration = timedelta(seconds=10)

        event = G(Event, name="event", end_time=None, start_time=start_time, duration=duration, host=self.host,
                  venue=self.venue)
        event.clean()
        self.assertEqual(event.end_time, event.start_time + event.duration)
