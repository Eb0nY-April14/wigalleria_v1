from django.urls import path
from . import views
from .views import LikeView, AddCommentView

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('like/<int:pk>', LikeView, name='like_product'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    # Wish List
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:pk>/', views.add_to_wishlist, name='add_to_wishlist'),
]
