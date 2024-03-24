from typing import Any

from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["signup-form"] = self.get_form()
        context["user"] = self.request.user
        return context
