from django.contrib import admin
from django.urls import path, include
# from .views import home


urlpatterns = [
    # path("", home, name="home"),
    path('admin/', admin.site.urls),
    path('animal/', include('animal.urls'), name='animal'),
    path('car/', include('car.urls'), name='car')
]
