from django.urls import path
from . import views
from .views import LikeView, AddCommentView

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('like/<int:pk>', LikeView, name='like_product'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:pk>/', views.add_to_wishlist, name='add_to_wishlist'),  # noqa
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete'),  # noqa
]
