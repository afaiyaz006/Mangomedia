from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/profile', views.profile, name='profile'),
    path('dummy/', views.dummy, name='dummy'),
    path('create_post/', views.create_post, name='create_post'),
    path('mango_posts/', views.view_post, name='mango_posts'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('load-more-posts/', views.load_more_posts, name='load_more_posts'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),

]