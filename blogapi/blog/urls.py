from django.urls import path, include
from . import views


urlpatterns = [
    path('posts/', views.get_all_posts),
    path('one/<int:id>/', views.get_single_post),
    path('create/', views.create_post),
    path('update/<int:id>/', views.update_post),
    path('delete/<int:id>/', views.delete_post),
    path('comments/<int:id>/', views.get_all_comments),
    path('post_comments/', views.post_comment),
    path('signup/', views.signup),
    path('allusers/', views.get_all_users),
]
