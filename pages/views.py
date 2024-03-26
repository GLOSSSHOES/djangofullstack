from typing import Any
from django.views.generic import TemplateView, ListView, FormView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import reverse_lazy
from shoes.models import Shoe
from .forms import ContactForm

class HomePageView(ListView):
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

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["form"] = self.form_class()
        return context
    
    def form_valid(self, form):
        # Process the form data (e.g., send email)
        # Here you can access the form data using form.cleaned_data
        # For demonstration purposes, let's just print the data to the console
        print(form.cleaned_data)
        return super().form_valid(form)

