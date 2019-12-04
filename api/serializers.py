from rest_framework import serializers
from listings.models import Listings


class ListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listings
        fields = ('id', 'title', 'price', 'list_date')
