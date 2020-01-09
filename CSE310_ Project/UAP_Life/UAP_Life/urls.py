"""UAP_Life URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views


urlpatterns = [
    path('', views.Home_Page),
    path('admin/', admin.site.urls),
    path('Main.html/', views.Main_Page),
    path('Main.html/post_ad.html/',views.post_ad),
    path('Main.html/questionbank_first_page.html/',views.question_bank),
    path('Main.html/questionbank_first_page.html/submit_question_page.html/',views.submit_question),
    path('Main.html/post_ad.html/post_ad2.html',views.post_ad2),

]
