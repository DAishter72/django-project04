from django.urls import path
from post.views import PostListView, PostCreateView, PostEditView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),  # List view for posts
    path('create/', PostCreateView.as_view(),
         name='post_create'),  # Create view for posts
    path('edit/<int:pk>/', PostEditView.as_view(),
         name='post_edit'),  # Edit view for posts
    path('delete/<int:pk>/', PostDeleteView.as_view(),
         name='post_delete'),  # Delete view for posts
]
