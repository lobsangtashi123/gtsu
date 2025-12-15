from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.index, name="index"),
        path('submit-valunteer/', views.submit_valunteer, name="submit-valunteer"),
        path('contact/', views.contact, name="contact"),
        path('volunteer/', views.volunteer, name="volunteer"),

        path('blog/', views.blog_list, name='blog_list'),
        path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
        path('about/', views.about, name='about'),
        path('announcements/', views.announcement_list, name='announcement_list'),
        path('announcements/<int:id>/', views.announcement_detail, name='announcement_detail'),
]
