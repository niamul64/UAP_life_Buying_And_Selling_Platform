from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:user_id>/', views.profile_view, name='user_profile'),
    path('logout/', views.user_logout, name='logout'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('question_bank/', include('question_bank.urls'), name='q_index'),
    path('asdf/<int:userr>/', views.postAD, name='postAD'),
    path('success/', views.success, name='success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
