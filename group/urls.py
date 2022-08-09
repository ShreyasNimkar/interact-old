from django.urls import path
from . import views


urlpatterns = [
    path('create/',views.create),
    path('createhandler/',views.createhandler),
    path('view/',views.view),
    path('view/<str:slug>',views.viewgrp),
    path('join/<str:slug>',views.joingrp),
    path('leave/<str:slug>',views.leavegrp),
    path('delete/<str:slug>',views.delete),
    path('joinchat/<str:slug>',views.joinchat),
    path('joinchat/<str:slug>/post',views.groupchat),
    path('joinchat',views.joinchat_blank),
]