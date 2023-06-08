"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from users import views as user_views


"""Checks for paths that lead to a HTTP response in views"""

urlpatterns = [
    # Sends a request for the empty path to views.home function
    path('', views.PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/delete/success', views.PostDeleteCompleteView.as_view(), name='post-delete-success'),
    # Sends a request for the about/ path to user_views.about function
    # path('about/', user_views.about, name="about"),
    # Create Explicit Admin Route if not specified
    path('admin/', admin.site.urls),
    # Create a registration Route
    path('register/', user_views.register, name="register"),
    # Create a profile Route
    path('profile/', user_views.profile, name="profile"),
    # Create a LOGIN Page route
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    #  as_view() allows to define a custom route to the login page rather than the default path
    #  i.e. registration/login.html or registration/logout.html

    # Create a LOG Out Page route
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name="password_reset_complete"),
    ]

# Means it is explicitly only to facilitate during development not during deployment (settings.DEBUG)
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
