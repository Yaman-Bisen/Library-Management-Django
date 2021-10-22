from app.models import BookDetails
from rest_framework.response import Response
from app.api.serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookDetails.objects.all()
    serializer_class = BookSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]



@api_view(['GET'])
def StudentInfo(request, user=None):
    if request.method == "GET":
        email = user
        if email is not None:
            books = BookDetails.objects.filter(user=email)
            serializer = BookSerializer(books,many=True)
            return Response(serializer.data)
        books = BookDetails.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
