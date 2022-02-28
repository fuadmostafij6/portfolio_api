
from django.contrib import admin
from django.urls import path,include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve
urlpatterns = [
    path('', admin.site.urls),
    path('api/banner/',include('banner.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/nav/',include('nav.urls')),
    path('api/intro/',include('intro.urls')),
    path('api/skill/', include('skill.urls')),
    path('api/portfolio/', include('portfolio.urls')),
    path('api/contact/', include('contact.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



