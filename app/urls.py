from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('contact/', views.ContactUs, name='contact'),
    path('contact/send/', views.ContactSend, name='contact_send'),
    path('thumbnails/', views.Files, name='files'),
    path('media/', views.Media, name="media"),
    path('post/search/', views.SearchPosts, name='sposts'),
    path('posts/details/<slug:slug>/', views.DetailsPosts, name='details'),
    path('richtexteditor/', views.richTextField, name='richTextField'),
    path('media/url/', views.MediaUrl, name='media_url'),
]