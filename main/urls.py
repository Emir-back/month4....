from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/',include('first_lesson.urls')),
    path('films/', include('films.urls')),
    path('tags/', include('tags.urls')),
    path('parser/', include('parser_app.urls')),
    path('users/', include('users.urls')),
    path('', include('foods.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
