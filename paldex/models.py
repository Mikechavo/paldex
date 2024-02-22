from django.db import models
from django.utils.translation import gettext as _

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class PalModel(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    image = models.ImageField(upload_to='images/')
    type = models.CharField(_("Type"), max_length=200)
    skill = models.CharField(_("Skill"), max_length=200)
    work = models.CharField(_("Work"), max_length=200)
    drops = models.CharField(_("Drops"), max_length=200)
    price = models.BigIntegerField(_("Price"))

    def __str__(self):
        return self.name