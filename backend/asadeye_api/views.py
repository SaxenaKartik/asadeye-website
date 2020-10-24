from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from asadeye_api import models
from asadeye_api import serializers
from rest_framework.authentication import TokenAuthentication
from asadeye_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating users"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)

    def list(self, request):
        queryset = models.UserProfile.objects.all()
        name = request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name = name)
        serializer = serializers.UserProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('id', 'name', 'email', 'phone_no',)

class UserLoginAPIView(ObtainAuthToken):
    """ Handle creating user auth token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    # since ObtainAuthToken class doesn't have renderer_classes defined

class ProductViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating products"""
    serializer_class = serializers.ProductSerializer
    queryset = models.Products.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('id', 'product_name', 'product_price', 'product_desc',)


class ImageViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating images"""
    serializer_class = serializers.ImageSerializer
    queryset = models.Images.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('id', 'image_name','product_id')