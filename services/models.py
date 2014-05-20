from django.db import models


class Service(models.Model):
    """
    Model to store a service and it's price
    """
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def str(self):
        return self.name, self.price
