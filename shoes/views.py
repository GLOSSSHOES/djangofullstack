from typing import Any

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
        context["shoes"] = Shoe.objects.all()
        context["user"] = self.request.user
        return context
