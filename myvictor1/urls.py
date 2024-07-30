"""
URL configuration for myvictor1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static 
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('chat/', include('chat.urls')),
    path('schools/', include('schools.urls')),    
    path('student_management/', include('student_management.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('academic/', include('academic.urls')),
    path('Extracurricular/',include('Extracurricular.urls')),
    path('authorization/',include('authorization.urls')),
     
    
    
         
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
