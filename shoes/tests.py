from django.test import TestCase
from django.urls import reverse
from .models import Shoe


class ShoeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.shoe = Shoe.objects.create(
            name="model1",
            company="keyla",
            description="Descripción 1",
            price="30000",
            image="shoes/shoe1_Gct7Wxy.jpeg",
        )

    def test_shoe_listing(self):
        self.assertEqual(f"{self.shoe.name}", "model1")
        self.assertEqual(f"{self.shoe.company}", "keyla")
        self.assertEqual(f"{self.shoe.price}", "30000")

    def test_shoe_list_view(self):
        response = self.client.get(reverse("shoe_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "model1")
        # self.assertTemplateUsed(response, "shoes/shoe_list.html")

    def test_shoe_detail_view(self):
        response = self.client.get(self.shoe.get_absolute_url())
        no_response = self.client.get("/shoes/111")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "model1")
        self.assertContains(response, "shoes/shoe_detail.html")
