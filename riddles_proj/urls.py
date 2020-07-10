from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('riddles_app/', include('riddles_app.urls'), name='riddles_app'),
]
