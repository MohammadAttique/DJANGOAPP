from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderDetailViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'order-details', OrderDetailViewSet, basename='order-detail')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    # path('api/orders/', OrderViewSet.as_view({'post': 'create'}), name='order-create'),
    # Add other app URLs here
]
