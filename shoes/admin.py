from django.contrib import admin

from .models import Shoe


class ShoeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "company",
        "description",
        "price",
        "image",
    )


admin.site.register(Shoe, ShoeAdmin)
