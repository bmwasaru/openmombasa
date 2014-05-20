from django.forms import widgets
from rest_framework import serializers
from services.models import Service


class ServiceSerializer(serializers.Serializer):

    id = serializers.Field()
    name = serializers.Field()
    price = serializers.Field()

    class Meta:
        model = Service

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
