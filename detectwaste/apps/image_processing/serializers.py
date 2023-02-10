from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Category, ProcessedImage


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "slug"]


class ProcessedImageSerializer(ModelSerializer):
    created = ReadOnlyField()
    processed = ReadOnlyField()
    status = ReadOnlyField()
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = ProcessedImage
        fields = ["id", "image", "created", "processed", "status", "categories"]
