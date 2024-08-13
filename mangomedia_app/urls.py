from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mangoposts',views.mango_posts,name='mango_posts'),
    path('accounts/profile/',views.profile,name='profile'),

]