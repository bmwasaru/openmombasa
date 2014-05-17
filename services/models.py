from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def str(self):
        return self.name, self.price