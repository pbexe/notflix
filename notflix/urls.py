"""The master router for the whole project
"""

from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^', include('movies.urls', namespace='movies')),
    url(r'^users/', include('users.urls')),
    url(r'^orders/', include('orders.urls', namespace='orders')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
