from django.urls import path
from checkInCheckOut.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    # path('', views.index,name='index'),
  path('check_in_out/', check_in_out, name='check_in_out'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)