"""warehouse_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from warehouse_app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    # gatunki stali
    path('grades/', views.grade_list),
    path('grades/<int:id>', views.grade_detail),
    # średnice prętów
    path('dimensions/', views.dimension_list),
    path('dimensions/<int:id>', views.dimension_detail),
    # średnice prętów
    path('bars/', views.bar_list),
    path('bars/<int:id>', views.bar_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
