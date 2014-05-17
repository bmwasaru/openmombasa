from django.forms import widgets
from rest_framework import serializers
from services.models import Service


class ServiceSerializer(serializers.Serializer):
    pk = serializers.Field()  # field is untyped read only
    name = serializers.CharField(max_length=100)
    price = serializers.CharField(max_length=100)

    def restore_object(self, attrs, instance=None):
        """
        Creates or update an new service instance, given a dictionary of deserialized field values
        """
        if instance:
            #  update existing instance
            instance.name = attrs.get('name', instance.name)
            instance.price = attrs.get('price', instance.price)

        # create new instance
        return Service(**attrs)