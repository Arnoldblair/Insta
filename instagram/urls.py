from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.urls import path
from instagram.views import home_view, register,login_view, logout_view

urlpatterns=[
    path('',home_view, name="dashboard"),
    path('register/', register, name="register"),
    path('login/', login_view, name="login"),
    path('login/', logout_view, name="logout")

    ]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)    