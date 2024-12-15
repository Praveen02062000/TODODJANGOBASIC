from rest_framework import serializers
from .models import TODOTABLE


class TODOSERIALIZER(serializers.ModelSerializer):
    class Meta:
        model=TODOTABLE
        fields=("id","todovalue","todostatus")


