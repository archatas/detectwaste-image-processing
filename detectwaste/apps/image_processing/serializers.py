from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Category, ProcessedImage


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "slug"]


class ProcessedImageSerializer(ModelSerializer):
    created_at = ReadOnlyField()
    processed_at = ReadOnlyField()
    status = ReadOnlyField()
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = ProcessedImage
        fields = ["id", "image", "created_at", "processed_at", "status", "categories"]
