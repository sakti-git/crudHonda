"""crudHonda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showProd, name="showProd"),
    path('Insert', views.insertMotor, name="insertMotor"),
    path('Edit/<int:id>', views.editMotor, name="editMotor"),
    path('Update/<int:id>', views.updateProd, name="updateProd"),
    path('Delete/<int:id>', views.deleteProd, name="deleteProd")
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
