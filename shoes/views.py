import json
import hashlib

from typing import Any

from django.http import HttpRequest, HttpResponse

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
        return context


class ShoePurchaseConfirmationWAddress(DetailView):
    model = Shoe
    context_object_name = "shoe"
    template_name = "shoes/shoe_purchase_conf_with_addresses.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        reqP = request.POST
        context = {}
        context["user"] = request.user
        context["shoe"] = self.get_object()
        context["address"] = reqP.get("address")
        context["city"] = reqP.get("city")
        context["state"] = reqP.get("state")
        context["zip_code"] = reqP.get("zip_code")
        context["email"] = reqP.get("email")
        context["MERCHANT_IDDev"] = PayuCredentialsDev().CREDENTIALS["MERCHANT_ID"]
        context["USER_IDDev"] = PayuCredentialsDev().CREDENTIALS["USER_NICOLAS_ID"]
        context["signature"] = self.hashes_signature()
        return self.render_to_response(context=context)

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
