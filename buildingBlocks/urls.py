from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Custom Pc",
      default_version='v1',
      description="Test description",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('orders',views.OrderView.as_view(), name='orders'),
    path('orders/<int:pk>',views.OrderEdit.as_view(), name='orders-edit'),
    path('orders/create', views.OrderAdd.as_view(), name='create-order'),
    path('orders/components/<int:pk>', views.OrderItemEdit.as_view(), name='order-item-update'),
    path('orders/order',views.OrderItemsCreate.as_view(), name='order-items-create'),
    path('cpu',views.CpuView.as_view(), name='cpu'),
    path('cpu/<int:pk>',views.CpuViewEdit.as_view(), name='cpu-detail'),
    path('motherboard',views.MotherboardView.as_view(), name='motherboard'),
    path('motherboard/<int:pk>',views.MotherboardEdit.as_view(), name='motherboard-detail'),
    path('gpu',views.GpuView.as_view(), name='gpu'),
    path('gpu/<int:pk>',views.GpuViewEdit.as_view(), name='gpu-detail'),
    path('brand',views.BrandNamesListView.as_view(), name='brand'),
    path('brand/<int:pk>',views.BrandNamesDetailView.as_view(), name='brand-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]