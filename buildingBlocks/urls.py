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
    path('os',views.OsView.as_view(), name='os'),
    path('os/<int:pk>',views.OsEdit.as_view(), name='os-detail'),
    path('motherboard',views.MotherboardView.as_view(), name='motherboard'),
    path('motherboard/<int:pk>',views.MotherboardEdit.as_view(), name='motherboard-detail'),
    path('gpu',views.GpuView.as_view(), name='gpu'),
    path('gpu/<int:pk>',views.GpuViewEdit.as_view(), name='gpu-detail'),
    path('wifi',views.WifiView.as_view(), name='wifi'),
    path('wifi/<int:pk>',views.WifiEdit.as_view(), name='wifi-detail'),
    path('case',views.CaseView.as_view(), name='case'),
    path('case/<int:pk>',views.CaseEdit.as_view(), name='case-detail'),
    path('cooler',views.CoolerView.as_view(), name='cooler'),
    path('cooler/<int:pk>',views.CoolerEdit.as_view(), name='cooler-detail'),
    path('ssd',views.SsdView.as_view(), name='ssd'),
    path('ssd/<int:pk>',views.SsdEdit.as_view(), name='ssd-detail'),
    path('hdd',views.HddView.as_view(), name='hdd'),
    path('hdd/<int:pk>',views.HddEdit.as_view(), name='hdd-detail'),
    path('psu',views.PsuView.as_view(), name='psu'),
    path('psu/<int:pk>',views.PsuEdit.as_view(), name='psu-detail'),
    path('ram',views.RamView.as_view(), name='ram'),
    path('ram/<int:pk>',views.RamEdit.as_view(), name='ram-detail'),
    path('monitor',views.MonitorView.as_view(), name='monitor'),
    path('monitor/<int:pk>',views.MonitorEdit.as_view(), name='monitor-detail'),
    path('keyboard',views.KeyboardView.as_view(), name='keyboard'),
    path('keyboard/<int:pk>',views.KeyboardEdit.as_view(), name='keyboard-detail'),
    path('headset',views.HeadsetView.as_view(), name='headset'),
    path('headset/<int:pk>',views.HeadsetEdit.as_view(), name='headset-detail'),
    path('mouse',views.MouseView.as_view(), name='mouse'),
    path('mouse/<int:pk>',views.MouseEdit.as_view(), name='mouse-detail'),
    path('brand',views.BrandNamesListView.as_view(), name='brand'),
    path('brand/<int:pk>',views.BrandNamesDetailView.as_view(), name='brand-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]