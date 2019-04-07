from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    path('categories/', views.index, name='categories'),
    # ex: /categories/math
    path('categories/<str:category_name>/', views.category_words, name='category_words'),
    # ex: /about
    path('about/', views.about, name='about'),
    path('stop_words/', views.stop_words, name='stop'),
]
