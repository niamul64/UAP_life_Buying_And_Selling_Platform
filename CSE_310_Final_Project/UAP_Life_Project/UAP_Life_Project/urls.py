
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import user_profile.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_profile.views.index, name='index'),
    path('signup/', user_profile.views.signup, name='signup'),
    path('loginpage/', user_profile.views.loginpage, name='loginpage'),
    path('login/', user_profile.views.log_in,name='login'),
    path('logout/', user_profile.views.user_logout, name='logout'),
    path('home',user_profile.views.home,name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
