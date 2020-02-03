from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('question_bank/', include('question_bank.urls'), name='q_index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
