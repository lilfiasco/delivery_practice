from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.auths.views import (
    CustomLoginView,
    CustomLogoutView,
   
)
from django.urls import path
from apps.main.views import (
    get_base,
    get_index
)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    
    path('', include('main.urls')),
    path('/auth/', include('auths.urls')),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
