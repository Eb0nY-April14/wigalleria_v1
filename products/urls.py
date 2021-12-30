from django.urls import path
from . import views
from .views import LikeView

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('like/<int:pk>', LikeView, name='like_product'),
]
