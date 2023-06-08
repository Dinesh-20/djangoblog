from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about')
]

# by default to present this view it looks for a template with name as
# <app>/<model>_<viewtype>.html
