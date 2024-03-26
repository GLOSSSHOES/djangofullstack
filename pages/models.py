import uuid
from django.db import models


class StakeholderMessage(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Tu nombre")
    email = models.EmailField(verbose_name="Tu correo electrónico")
    message = models.TextField(verbose_name="Tu inquietud")
    related_user = models.ForeignKey(
        "accounts.CustomUser", on_delete=models.DO_NOTHING, null=True, blank=True
    )
    user_is_anonymous = models.BooleanField(default=True)

    def __str__(self):
        return self.name
