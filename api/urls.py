from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("",views.apiOverview,name="Landing Page"),

    path("testmodel-detail/",views.TestModelView,name="Landing Page"),
    path("testmodel-create/",views.TestModelCreate,name="Landing Page"),
    path("testmodel-delete/<int:pk>/",views.TestModelDelete,name="Landing Page"),

    path("user-detail/",views.UserList,name="Landing Page"),
    path("user-create/",views.UserCreate,name="Landing Page"),
    path("user-detail/<str:username>/",views.UserDetail,name="Landing Page"),
    path("user-update/<str:username>/",views.UserUpdate,name="Landing Page"),
    path("user-delete/<str:username>/",views.UserDelete,name="Landing Page"),

    path("group-detail/",views.GroupList,name="Landing Page"),

    path("post-create/",views.UserPost,name="Landing Page"),
    path("post-detail/<str:username>/",views.UserPostList,name="Landing Page"),
    path("comment-detail/",views.CommentList,name="Landing Page"),
]