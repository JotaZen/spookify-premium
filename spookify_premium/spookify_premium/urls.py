
from django.contrib import admin
from django.urls import path, include
from apps.music_library.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='inicio'),
    path('biblioteca/', include('apps.music_library.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'apps.music_library.views.view_404'
