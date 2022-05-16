from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,AddCommentView
from . import views

urlpatterns = [
    path('', PostListView.as_view(),name="home_page-home"),
    path('post/<int:pk>/', PostDetailView.as_view(),name="post-detail"),
    path('post/new/', PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name="post-delete"),
    path('post/<int:pk>/comment/', AddCommentView.as_view(),name="add-comment"),
    path("welcome/",views.welcome,name ="home_page-welcome"),
]