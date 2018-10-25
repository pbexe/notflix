
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('movies.urls', namespace='movies')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
