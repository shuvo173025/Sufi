"""sufi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.core.views import frontpage, signup
from apps.conversation.views import conversations, conversation
from django.contrib.auth import views
from apps.feed.views import feed,search
from apps.conversation.api import api_add_message
from apps.feed.api import api_add_post, api_add_like

from apps.userprofile.views import userprofile, follow_user, unfollow_user, followers, follows, edit_profile

urlpatterns = [
    path('', frontpage, name='frontpage'),

    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(),name='logout'),
    path('login/', views.LoginView.as_view(template_name = 'core/login.html'),name='login'),

    path('edit_profile/', edit_profile, name='edit_profile'),


    path('feed/', feed, name='feed'),
    path('search/', search, name='search'),

    path('u/<str:username>/', userprofile, name= 'userprofile'),

    path('u/<str:username>/follow/',follow_user, name='follow_user'),
    path('u/<str:username>/unfollow/',unfollow_user, name='unfollow_user'),
    path('u/<str:username>/followers/',followers, name='followers'),
    path('u/<str:username>/follows/',follows, name='follows'),

    path('conversations/', conversations, name='conversations'),
    path('conversations/<int:user_id>/', conversation, name='conversation'),

    path('api/add_post/',api_add_post,name='api_add_post'),
    path('api/add_like/',api_add_like,name='api_add_like'),
    path('api/add_message/', api_add_message, name='api_add_message'), 


    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
