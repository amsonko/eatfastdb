from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
# userrouter = routers.DefaultRouter()
# userrouter.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
#     url(r'^', include(userrouter.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('dbservices.urls')),
]