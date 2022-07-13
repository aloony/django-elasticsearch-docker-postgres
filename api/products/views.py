from rest_framework.viewsets import ModelViewSet
from products.models import Product
from products import serializers

class ProductViewSet(ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()



