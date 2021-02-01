"""skilljag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path

from django.conf import settings
from django.conf.urls.static import static

from django_registration.backends.activation.views import RegistrationView

from core.views import IndexTemplateView
from profiles.forms import UserRegistrationForm


urlpatterns = [
    path('admin/', admin.site.urls),

    path("accounts/register/",
         RegistrationView.as_view(
             form_class=UserRegistrationForm,
             ), name="django_registration_register"), 

    path("accounts/",
         include("django_registration.backends.activation.urls")),

    path("accounts/",
         include("django.contrib.auth.urls")),

    path("api/",
         include("core.api.urls")),

    path("api/",
         include("profiles.api.urls")),

    path("api/",
         include("feed.api.urls")),

    path("api-auth/",
         include("rest_framework.urls")),

    path("api/rest-auth/",
         include("rest_auth.urls")),
        
    path("api/rest-auth/registration/",
         include("rest_auth.registration.urls"))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [ re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"), ]
