from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('orders',views.OrdersView.as_view()),
    path('orders/create', views.CreateOrderView.as_view(), name='create-order'),
    path('orders/<int:pk>',views.OrdersDetailView.as_view()),
    path('cpu',views.CpuListView.as_view()),
    path('cpu/<int:pk>',views.CpuListDetailView.as_view()),
    path('brand',views.BrandNamesListView.as_view()),
    path('brand/<int:pk>',views.BrandNamesDetailView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('select-parts/', views.SelectComponentsView.as_view(), name='select-components'),
]