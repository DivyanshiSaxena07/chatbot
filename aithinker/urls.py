"""
URL configuration for aithinker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from chatapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='home'),
    path("signin/",admin_login,name="login"),
    # path("signup/",signup,name="signup"),
    path("logout/",user_logout,name="logout"),
    path("chatbox/",view_history,name="chatbox"),
    path("formData.txt",read_file,name="read")
    # path("add/",upload,name="add"),
    
   
    
]
