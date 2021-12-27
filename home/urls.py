from django.urls import path
from . import views

# The index used here is same as store used
# in the Django tutorial on YouTube
urlpatterns = [
    path('', views.index, name='home')
]
