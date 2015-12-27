from datetime import date

from django.test import TestCase

from django_dynamic_fixture import G

from elements.base.models import Place
from elements.commute.models import Vehicle, CommuteUser, Route, RouteLog, PickUpEvent


class VehicleModelTest(TestCase):
    """
    Class to test Vehicle model
    """

    @classmethod
    def setUpClass(cls):
        """
        Initial setup for test cases
        """

        cls.owner = G(CommuteUser, username="vehicle_user")
        cls.vehicle = G(Vehicle, owner=cls.owner)
        super(VehicleModelTest, cls).setUpClass()

    def test_create(self):
        """
        Test created object
        """

        # auto id set
        self.assertIsNotNone(self.vehicle.id)

    def test_str(self):
        """
        Test str return of object
        """

        self.assertEqual(str(self.vehicle),
                         "vehicle_user - {} - {}".format(self.vehicle.type, self.vehicle.license_number))


class RouteModelTest(TestCase):
    """
    Class to test Route model
    """

    @classmethod
    def setUpClass(cls):
        """
        Initial setup for test cases
        """

        cls.home = G(Place, name="home")
        cls.office = G(Place, name="office")
        cls.user = G(CommuteUser, username="route_user", home_location=cls.home, office_location=cls.office)
        cls.route = G(Route, user=cls.user)
        super(RouteModelTest, cls).setUpClass()

    def test_create(self):
        """
        Test created object
        """

        # auto id set
        self.assertIsNotNone(self.route.id)
        # User is set
        self.assertEqual(self.route.user, self.user)

    def test_str(self):
        """
        Test str return of object
        """

        self.assertEqual(str(self.route),
                         "route_user : {} to {}".format(self.route.start_location, self.route.end_location))


class RouteLogModelTest(TestCase):
    """
    Class to test RouteLog model
    """

    @classmethod
    def setUpClass(cls):
        """
        Initial setup for test cases
        """

        cls.home = G(Place, name="home")
        cls.office = G(Place, name="office")
        cls.user = G(CommuteUser, username="route_log_user", home_location=cls.home, office_location=cls.office)
        cls.route = G(Route, user=cls.user)
        cls.route_log = G(RouteLog, route=cls.route, date=date.today())
        super(RouteLogModelTest, cls).setUpClass()

    def test_create(self):
        """
        Test created object
        """

        # auto id set
        self.assertIsNotNone(self.route_log.id)
        # Route is set
        self.assertEqual(self.route_log.route, self.route)
        # Date is set
        self.assertEqual(self.route_log.date, date.today())

    def test_str(self):
        """
        Test str return of object
        """

        self.assertEqual(str(self.route_log), "{route} : Dated {date}".format(route=self.route_log.route,
                                                                              date=date.today()))


class PickUpModelTest(TestCase):
    """
    Unit Test cases for Pick Up model
    """

    @classmethod
    def setUpClass(cls):
        """
        Initial setup for test cases
        """

        cls.route_log = G(RouteLog)
        cls.pickup_event = G(PickUpEvent, route=cls.route_log)
        super(PickUpModelTest, cls).setUpClass()

    def test_create(self):
        """
        Test created object
        """

        # auto id set
        self.assertIsNotNone(self.pickup_event.id)
        # RouteLog is set
        self.assertEqual(self.pickup_event.route, self.route_log)
