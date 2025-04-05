from django.urls import path
from post.views import PostListView, PostDetailView, PostCreateView, PostEditView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),  # List view for posts
    path('create/', PostCreateView.as_view(),
         name='post_create'),  # Create view for posts
    path('edit/<slug:slug>/', PostEditView.as_view(),
         name='post_edit'),  # Edit view for posts
    path('delete/<slug:slug>/', PostDeleteView.as_view(),
         name='post_delete'),  # Delete view for posts
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
