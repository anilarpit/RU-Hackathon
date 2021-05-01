"""myRevisor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from Profile.views import update_profile, register, login_out, login_in
from notes.views import note_create_view, get_notes

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register),
    path('home/', register, name='home'),
    path('register/', register, name='register'),
    path('profile/', update_profile, name='update_profile'),
    path('create_note/', note_create_view, name='create_notes'),
    path('note/', get_notes, name='notes'),
    path('logout/', login_out, name='login_out'),
    path('login_in/', login_in, name='login_in'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
