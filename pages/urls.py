from django.urls import path
from .views import HomePageView, BrandView, CreateStakeHolderMessage

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("contacto/", CreateStakeHolderMessage.as_view(), name="contact"),
    path("marca/", BrandView.as_view(), name="brand"),
]
