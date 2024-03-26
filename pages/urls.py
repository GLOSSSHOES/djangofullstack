from django.urls import path
from .views import HomePageView, ContactFormView, BrandView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("contacto/", ContactFormView.as_view(), name="contact"),
    path("marca/", BrandView.as_view(), name="brand"),
]
