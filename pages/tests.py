from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from .views import HomePageView, BrandView, CreateStakeHolderMessage
from .models import StakeholderMessage


class HomepTests(TestCase):
    def setUp(self):  # new
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertEquals(self.response.template_name[0], "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Nuestros modelos")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self):  # new
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class BrandTests(SimpleTestCase):  # new
    def setUp(self):
        url = reverse("brand")
        self.response = self.client.get(url)

    def test_brandpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_brandpage_template(self):
        self.assertEquals(self.response.template_name[0], "brand.html")

    def test_brandpage_contains_correct_html(self):
        self.assertContains(self.response, "Quiénes somos?")

    def test_brandpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_brandpage_url_resolves_aboutpageview(self):
        view = resolve("/marca/")
        self.assertEqual(view.func.__name__, BrandView.as_view().__name__)


class ContactTests(SimpleTestCase):  # new
    def setUp(self):
        url = reverse("contact")
        self.response = self.client.get(url)

    def test_brandpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_brandpage_template(self):
        self.assertEquals(self.response.template_name[0], "contact.html")

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, "¿Cómo contactarnos?")

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "No nos escribas")

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve("/contacto/")
        self.assertEqual(
            view.func.__name__, CreateStakeHolderMessage.as_view().__name__
        )


class ContactFormTestCase(TestCase):
    def test_contact_form_submission(self):
        # Create test data for form submission
        form_data = {
            "name": "Test User",
            "email": "test@example.com",
            "message": "Test message",
        }

        # Submit the form data
        response = self.client.post(reverse("contact"), form_data)

        # Check if the form submission was successful and redirected to the success URL
        self.assertEqual(
            response.status_code, 302
        )  # 302 is the status code for redirection

        # Check if the message was saved correctly in the database
        self.assertTrue(
            StakeholderMessage.objects.filter(
                name=form_data["name"],
                email=form_data["email"],
                message=form_data["message"],
            ).exists()
        )
