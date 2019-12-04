from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView

from listings.models import Listings
from .serializers import ListingsSerializer, DetailsSerializer


@api_view(['GET'])
def get_listings(request):
    if request.method == "GET":
        active_listings = Listings.objects.filter(is_published=True)[:10]
        serializer = ListingsSerializer(active_listings, many=True)
        return Response(serializer.data)


class ListDetailView(RetrieveAPIView):
    queryset = Listings.objects.filter(is_published=True)
    serializer_class = DetailsSerializer
