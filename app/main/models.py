from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

from regions.models import City


# Create your models here.

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return f'uploads/hakaton_images/{filename}'

class Hakaton(models.Model):

    preview = models.FileField(
        _("Фотография"),
        upload_to=get_file_path
    )
    description = models.TextField(max_length=300)
    prize_fund = models.BigIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.ForeignKey(City, on_delete=models.CASCADE)


class Hakaton2(models.Model):

    preview = models.FileField(
        _("Фотография"),
        upload_to=get_file_path
    )
    description = models.TextField(max_length=300)
    prize_fund = models.BigIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.ForeignKey(City, on_delete=models.CASCADE)