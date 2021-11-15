from django.conf.urls import url
from StudentsApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^classes/$', views.classesApi),
    url(r'^classes/([0-9]+)$', views.classesApi),
    url(r'^students/$', views.studentsApi),
    url(r'^students/([0-9]+)$', views.studentsApi),
    url(r'^SavePhoto$', views.SavePhoto)
] + static(settings.PHOTO_URL, document_root=settings.MEDIA_ROOT)