from app.models import BookDetails
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = '__all__'