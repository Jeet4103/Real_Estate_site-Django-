from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from listings.views import Listing_list , listing_reterive, listing_create , listing_update , listing_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Listing_list),
    path('listings/<id>/',listing_reterive),
    path('add-listing/',listing_create),
    path('listings/<id>/edit/',listing_update),
    path('listings/<id>/delete/',listing_delete)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)