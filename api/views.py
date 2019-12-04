from rest_framework.response import Response
from rest_framework.decorators import api_view

from listings.models import Listings
from .serializers import ListingsSerializer


@api_view(['GET'])
def get_listings(request):
    if request.method == "GET":
        active_listings = Listings.objects.filter(is_published=True)[:10]
        serializer = ListingsSerializer(active_listings, many=True)
        return Response(serializer.data)
