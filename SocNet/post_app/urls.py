from django.urls import path
from .views import PostCreationView, MyPostsView, PostDeletionView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("create_post/", login_required(PostCreationView.as_view()), name = "create_post"),
    path('my_posts/', login_required(MyPostsView.as_view()), name= 'my_posts'),
    path('delete_post/', login_required(PostDeletionView.as_view()), name= 'delete_post')
]