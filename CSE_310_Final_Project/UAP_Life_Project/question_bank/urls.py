from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.q_index, name='q_index'),
    path('submit_q', views.submit_question, name='submit_q'),
    path('browse_q', views.browse_question, name='browse_q'),
    path('browse_q/<int:question_id>', views.full_question, name='full_question'),
    path('submit_answer/<int:question_id>', views.submit_answer, name='submit_answer'),
    path('full_answer/<int:answer_id>', views.full_answer, name='full_answer'),
    path('must_authenticate', views.must_authenticate, name='must_authenticate'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
