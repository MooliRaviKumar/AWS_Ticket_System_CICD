from django.contrib import admin
from django.urls import path, include
from tickets.views import FileUploadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('tickets.urls')),
    path('api/upload/', FileUploadView.as_view(), name='file-upload'),
]




