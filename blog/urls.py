from django.urls import path
from blog import views

appname = 'blog'

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/newpost/',views.CreatePostView.as_view(),name='create_post'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(),name='update_post'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='delete_post'),
    path('post/drafts/',views.DraftListView.as_view(),name='post_drafts'),
    path('post/<int:pk>/publish/',views.publish_post,name='publish_post'),
    path('post/<int:pk>/addcomment',views.add_post_comment,name='add_comment'),
    path('comment/<int:pk>/publish/',views.publish_comment,name='publish_comment'),
    path('comment/<int:pk>/delete/',views.delete_comment,name='delete_comment'),
] 