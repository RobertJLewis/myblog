from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include the blog app's URLs
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Serve static files in development



# build templates
