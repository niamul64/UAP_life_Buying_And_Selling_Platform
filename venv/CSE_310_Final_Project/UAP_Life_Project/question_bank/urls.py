from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.q_index, name='q_index'),
    path('submit_q', views.submit_question,name='submit_q'),
    path('browse_q',views.browse_question,name='browse_q'),
    path('must_authenticate', views.must_authenticate,name='must_authenticate'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
