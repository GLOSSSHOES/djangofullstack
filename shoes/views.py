import json
import hashlib

from typing import Any

from djangofullstack.settings.PAYU import PayuCredentialsProd, PayuCredentialsDev
from django.views.generic import ListView, DetailView
from .models import Shoe


class ShoeListView(ListView):
    model = Shoe
    context_object_name = "shoes"
    template_name = "shoes/shoe_list.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["shoes"] = Shoe.objects.all()
        context["user"] = self.request.user
        return context


class ShoeDetailView(DetailView):
    model = Shoe
    context_object_name = "shoe"
    template_name = "shoes/shoe_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


class ShoePurchase(DetailView):

    model = Shoe
    context_object_name = "shoe"
    template_name = "shoes/shoe_purchase.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["MERCHANT_IDDev"] = PayuCredentialsDev().CREDENTIALS["MERCHANT_ID"]
        context["USER_IDDev"] = PayuCredentialsDev().CREDENTIALS["USER_NICOLAS_ID"]
        context["signature"] = self.hashes_signature()
        return context

    def hashes_signature(self):
        input_bytes = self.creates_payment_signature_dev().encode("utf-8")
        hashed = hashlib.sha256(input_bytes)
        return hashed.hexdigest()

    def creates_payment_signature_dev(self):
        payucreds = PayuCredentialsDev.CREDENTIALS
        o_shoe = self.get_object()
        creds = [
            payucreds["API_KEY"],
            payucreds["MERCHANT_ID"],
            "PAGO003",
            str(o_shoe.price),
            "COP",
        ]
        return "~".join(creds)

    def creates_payment_signature_prod(self):
        payucreds = PayuCredentialsProd.CREDENTIALS
        o_shoe = self.get_object()
        creds = [
            payucreds["API_KEY"],
            payucreds["MERCHANT_ID"],
            str(o_shoe.pk),
            str(o_shoe.price),
            "COP",
        ]
        return "~".join(creds)
