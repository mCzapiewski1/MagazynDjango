"""magazyndjango URL Configuration

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
from django.contrib import admin
from django.urls import path
from inventory.views import home_view, showitems_view, additems_view, delitems, edititem
from authent.views import register_view, login_view, logoutUser

urlpatterns = [
    #common
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    #auth
    path('login/', login_view, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', register_view, name='register'),
    #inventory
    path('showitems/', showitems_view, name='showitems'),
    path('additems/', additems_view, name='additems'),
    path('delitem/<int:id>', delitems, name='delitem'),
    path('edititem/<int:id>', edititem, name='edititem')

]
