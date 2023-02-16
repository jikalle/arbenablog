from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home-index'),
    path('post/<slug:slug>/', views.PostDetail, name='post-detail'),
    path('edit/<slug:slug>/', views.edit_post, name='edit-post'),
    path('create_form/', views.create_post, name='create-post'),
]