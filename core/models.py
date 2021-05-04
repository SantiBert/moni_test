import uuid

from autoslug import AutoSlugField
from django.db import models
from django.utils import timezone


class Lending(models.Model):
    gender_choices = (
        ("HOMBRE", "HOMBRE"),
        ("MUJER", "MUJER"),
        ("PREFIERO NO DECIR", "PREFIERO NO DECIR"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre", max_length=150)
    slug = AutoSlugField(populate_from='id')
    last_name = models.CharField("Apellido", max_length=150)
    dni = models.PositiveIntegerField("Dni")
    gender = models.CharField("Género", max_length=80, choices=gender_choices)
    email = models.EmailField("E-mail", max_length=150)
    amount = models.PositiveIntegerField("Monto")
    status = models.BooleanField("Status", default=False)
    created_date = models.DateTimeField(default=timezone.now)
    error = models.BooleanField("Errores", default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.last_name
