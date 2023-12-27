from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page, about_page, contact_page, login_page, register_page
from monsters.views import MonsterListView, monster_list_view, MonsterDetailView, monster_detail_view

urlpatterns = [
        path('', home_page),
        path('about/', about_page),
        path('login/', login_page),
        path('register/', register_page),	 
        path('contact/', contact_page),
        path('monsters/', MonsterListView.as_view()),
        path('monsters-fbv/', monster_list_view),  
        path('monsters/<int:pk>', MonsterDetailView.as_view()),
        path('monsters-fbv/<int:pk>', monster_detail_view),   
        path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)