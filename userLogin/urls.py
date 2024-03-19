from django.urls import path
from userLogin.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    # path('', views.index,name='index'),
  path('login/', user_login, name='login'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)