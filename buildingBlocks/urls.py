from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('orders',views.OrdersView.as_view(), name='orders'),
    path('orders/create', views.CreateOrderView.as_view(), name='create-order'),
    path('orders/<int:pk>',views.OrdersDetailView.as_view(), name='order-detail'),
    path('cpu',views.CpuListView.as_view(), name='cpu'),
    path('cpu/<int:pk>',views.CpuListDetailView.as_view(), name='cpu-detail'),
    path('brand',views.BrandNamesListView.as_view(), name='brand'),
    path('brand/<int:pk>',views.BrandNamesDetailView.as_view(), name='brand-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('select-parts/', views.SelectComponentsView.as_view(), name='select-components'),
]