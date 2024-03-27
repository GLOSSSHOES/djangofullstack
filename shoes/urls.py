from django.urls import path
from .views import (
    ShoeListView,
    ShoeDetailView,
    ShoePurchase,
    ShoePurchaseConfirmationWAddress,
)

urlpatterns = [
    path("", ShoeListView.as_view(), name="shoe_list"),
    path("<uuid:pk>", ShoeDetailView.as_view(), name="shoe_detail"),
    path("<uuid:pk>/purchase/", ShoePurchase.as_view(), name="shoe_purchase"),
    path(
        "<uuid:pk>/confirmation/",
        ShoePurchaseConfirmationWAddress.as_view(),
        name="shoe_purchase_conf_with_addresses",
    ),
]
