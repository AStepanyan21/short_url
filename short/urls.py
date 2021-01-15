from django.urls import path

from . import views

urlpatterns = [
    path('', views.url_set, name='index'),
    path('<url>/', views.get_short_url, name='detail'),

]