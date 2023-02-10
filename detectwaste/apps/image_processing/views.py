from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import ProcessedImage
from .serializers import ProcessedImageSerializer


class ImageUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ProcessedImageSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            data = {"processed_image": instance.get_api_endpoint_url()}
            # TODO: trigger the processing of the image in the background
            # For example, you can use Celery or Huey for the background tasks
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProcessedImageList(generics.ListCreateAPIView):
    queryset = ProcessedImage.objects.all()
    serializer_class = ProcessedImageSerializer


class ProcessedImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProcessedImage.objects.all()
    serializer_class = ProcessedImageSerializer