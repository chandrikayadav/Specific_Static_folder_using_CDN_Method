"""
URL configuration for project14 project.

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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chandu2/',chandu2,name='chandu2'),
    path('chandu1/',chandu1,name='chandu1'),
    path('chandu3/',chandu3,name='chandu3'),
    path('chandu4/',chandu4,name='chandu4'),
    path('chandu5/',chandu5,name='chandu5'),
    path('chandu6/',chandu6,name='chandu6'),
    path('chandu7/',chandu7,name='chandu7'),
    path('chandu8/',chandu8,name='chandu8'),
    path('chandu9/',chandu9,name='chandu9'),
    path('chandu10/',chandu10,name='chandu10'),
    path('chandu11/',chandu11,name='chandu11'),
    path('chandu12/',chandu12,name='chandu12'),
    path('chandu13/',chandu13,name='chandu13'),
    path('chandu14/',chandu14,name='chandu14'),
    path('chandu15/',chandu15,name='chandu15'),
    path('chandu16/',chandu16,name='chandu16'),
    path('chandu17/',chandu17,name='chandu17'),
    path('chandu18/',chandu18,name='chandu18'),
    path('chandu19/',chandu19,name='chandu19'),
    path('chandu20/',chandu20,name='chandu20'),
    path('chandu21/',chandu21,name='chandu21'),
    path('chandu22/',chandu22,name='chandu22'),
    path('chandu23/',chandu23,name='chandu23'),
    path('chandu24/',chandu24,name='chandu24'),
    path('chandu25/',chandu25,name='chandu25'),
    path('chandu26/',chandu26,name='chandu26'),
    
]
