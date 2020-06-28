"""visual_helper_be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.conf.urls import url, include # django 2.부터 url 대신 path사용한다고 함
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="ImageCaptioning test open api",
        default_version="0.1",
        description="ImageCaptioning test open api 다큐먼테이션",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="angelic805@gmail.com"),
        license=openapi.License(name="APACHE 2.0"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^imgcaptioning', include(('imgcaptioning.urls', 'imgcaptioning'), namespace='imgcaptioning_api')),    
    # Auto DRF API docs
    re_path(r'^swagger(?P<format>\.json|\.yaml)/v1$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/v1$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/v1$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),    
]