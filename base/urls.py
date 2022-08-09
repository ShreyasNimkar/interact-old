from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="Landing Page"),
    path('starthandle/',views.starthandler),
    path("signup/",views.signup),
    path("login/",views.log_in),
    path("signuphandler/",views.signuphandler),
    path("loginhandler/",views.log_inhandler),
    path("logout/",views.log_out),
]