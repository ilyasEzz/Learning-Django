from rest_framework import serializers

from listings.models import Listings
from contacts.models import Comment


class ListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listings
        fields = ('id', 'title', 'price', 'list_date')


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listings
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
