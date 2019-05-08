"""The master router for the whole project
"""

from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from adminplus.sites import AdminSitePlus

# Admin setup
admin.site = AdminSitePlus()
admin.autodiscover()


urlpatterns = [
    url(r'^notflixadmin/', admin.site.urls),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^stats/', include('stats.urls', namespace='stats')),
    url(r'^', include('movies.urls', namespace='movies')),
   #url(r'^users/', include('users.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

