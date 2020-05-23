from django.urls import path
from . import views
from .views import BlogListView,BlogDetailView


urlpatterns = [
    path('hello/',views.index,name="blogindex"),
    path('',BlogListView.as_view(), name='home'),
    path('post/<int:pk>/',BlogDetailView.as_view(), name='post_detail'),

]
