from importlib.resources import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
       #path('',views.welcome,name = 'welcome'),
    path('',views.index,name='index'),
     path('profile/(\d+)',views.profile,name='profile'),
    path('profile/update/(\d+)',views.update_profile,name='update_profile'),
    path('no profile/(\d+)',views.no_profile, name='no_profile'),
    path('search/', views.search_results, name='search_results'),
    path('new/image/(\d+)',views.new_image,name="new_image"),
    path('comment/(\d+)', views.comment, name='comment'),
    path('comment/like/(\d+)',views.like_pic,name="like_pic"),
    path('image/update/(\d+)',views.update_image,name='update_image'),
    path('profile/follow/(\d+)', views.follow, name='follow'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)