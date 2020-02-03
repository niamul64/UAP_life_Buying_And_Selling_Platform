from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.q_index,name='q_index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
