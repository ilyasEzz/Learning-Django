from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from contacts.models import Comment
from listings.models import Listings
from .serializers import ListingsSerializer, DetailsSerializer, CommentsSerializer


@api_view(['GET'])
def get_listings(request):
    if request.method == "GET":
        active_listings = Listings.objects.filter(is_published=True)[:10]
        serializer = ListingsSerializer(active_listings, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def comments(request, pk):
    if request.method == 'POST':
        serializer = CommentsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    else:
        comments = Comment.objects.filter(is_active=True)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)


class ListDetailView(RetrieveAPIView):
    queryset = Listings.objects.filter(is_published=True)
    serializer_class = DetailsSerializer
