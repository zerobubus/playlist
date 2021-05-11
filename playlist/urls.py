from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404, handler500 
from django.conf import settings
from django.conf.urls.static import static
from music import views


urlpatterns = [
   
    path("", include("music.urls")),
    path('admin/', admin.site.urls),
    path("account/login/", views.LoginView.as_view(), name="account_login"),
    path("account/signup/", views.SignupView.as_view(), name="account_signup"),
    path("account/", include("account.urls")),
]
