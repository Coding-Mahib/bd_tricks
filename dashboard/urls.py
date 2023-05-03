from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout')
]