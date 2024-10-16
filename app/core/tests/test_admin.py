from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class AdminSiteTest(TestCase):
    """test user model on admin user interface"""

    def setUp(self):
        """create admin and normal users"""
        self.client = Client()
        # create super user
        self.admin = get_user_model().objects.create_superuser(
            email="admin@outlook.com", password="135tgulgfyh4pass"
        )
        # login as super user
        self.client.force_login(self.admin)

        # create normal user
        self.user = get_user_model().objects.create_user(
            email="moka@outlook.com", password="dgfhddfgjghjdgjd"
        )

    def test_usermodel_on_dashboard(self):
        """check if user model is on admin dashboard"""
        url = reverse("admin:index")
        res = self.client.get(url)

        self.assertContains(res, "Users")

    def test_listed_users_changelist_pass(self):
        """check to see if normal user added are on change list"""
        url = reverse("admin:core_user_changelist")
        # sending get request
        res = self.client.get(url)

        # checkign for presence of user on page
        self.assertContains(res, self.user.email)

    def test_detail_change(self):
        """check for instance presence"""

        # formulate url and send get request
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        # check for form view
        self.assertEqual(res.status_code, 200)
