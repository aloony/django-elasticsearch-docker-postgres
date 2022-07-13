from django.urls import path, include
from rest_framework.routers import SimpleRouter
from products.views import ProductViewSet

router = SimpleRouter()
router.register(
    '',
    ProductViewSet,
    basename='products-crud'
)


urlpatterns = [
    path('products/', include(router.urls))
]