from typing import Any

from django.contrib.auth.models import AnonymousUser
from django.forms.models import BaseModelForm
from django.views.generic import TemplateView, ListView, CreateView
from django.http import HttpResponse
from django.urls import reverse_lazy

from shoes.models import Shoe
from .forms import StakeFolderMessageForm
from .models import StakeholderMessage


class HomePageView(ListView):
    model = Shoe
    context_object_name = "shoes"
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["shoes"] = Shoe.objects.all()
        context["user"] = self.request.user
        return context


class BrandView(TemplateView):
    template_name = "brand.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


class CreateStakeHolderMessage(CreateView):
    model = StakeholderMessage
    form_class = StakeFolderMessageForm
    template_name = "contact.html"
    success_url = reverse_lazy("contact")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if not isinstance(self.request.user, AnonymousUser):
            form.instance.related_user = self.request.user
            form.instance.user_is_anonymous = False
        return super().form_valid(form)

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["data"] = self.request.POST if self.request.method == "POST" else None
        return kwargs
