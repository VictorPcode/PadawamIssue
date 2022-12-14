from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]