from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('category/<slug:category>/',
         views.CategoryPostsListView.as_view(),
         name='category_posts'),

    path('posts/<int:post_id>/',
         views.PostView.as_view(),
         name='post_detail'),

    path('posts/create/',
         views.PostCreateView.as_view(),
         name='create_post'),

    path('posts/<int:post_id>/edit/',  # wait work...
         views.PostUpdateView.as_view(),
         name='edit_post'),

    path('posts/<int:post_id>/delete/',  # wait work...
         views.PostDeleteView.as_view(),
         name='delete_post'),

    path('posts/<int:post_id>/comment/',
         views.PostView.as_view(),
         name='add_comment'),
    path('posts/<int:post_id>/edit_comment/<int:comment_id>/',
         views.CommentUpdateView.as_view(),
         name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/<int:comment_id>/',
         views.CommentDeleteView.as_view(),
         name='delete_comment'),


    path('profile/edit/',
         views.UserUpdateView.as_view(),
         name='edit_profile'),
    path('profile/<username>/',
         views.UserProfileView.as_view(),
         name='profile'),
]
