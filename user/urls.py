from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('view/<str:username>/',views.profile),
    path('follow/<str:username>/',views.follow),
    path('unfollow/<str:username>/',views.unfollow),
    path('feed/',views.feed_self),
    path('feed/<str:username>',views.feed_others),
    path('post/<str:post_slug>/like',views.like_post),
    path('post/create',views.create_post),
    path('post/createhandler',views.create_posthandler),
    path('post/<str:post_slug>/delete',views.delete_post),
    path('post/<str:post_slug>/comment/create',views.addcomment),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)