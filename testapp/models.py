from django.db import models

# Create your models here.


class TestModel(models.Model):
    number = models.IntegerField(default=0)

    def __str__(self):
        return "pk: %s, number: %s" % (self.pk, self.number)
