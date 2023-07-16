import random

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, User
from .serializers import ProductSerializer
from .producer import publish
import requests


class ProductViewSet(viewsets.ModelViewSet):
    def list(self, request):  # /api/products/ - GET
        resp = requests.get("http://0.0.0.0:5000/api/products")
        return Response(resp.json())

    def create(self, request):  # /api/products/ - POST
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save(owner=request.user)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # /api/products/<int:pk>/ - GET
        products = Product.objects.get(id=pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data)

    def update(self, request, pk=None):  # /api/products/<int:pk>/ - PUT
        products = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=products, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):  # /api/products/<int:pk>/ - DELETE
        products = Product.objects.get(id=pk)
        products.delete()
        publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self, _):
        user = random.choice(User.objects.all())
        return Response({'id': user.id})
