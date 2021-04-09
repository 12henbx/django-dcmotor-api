from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import (
    AllStatusViewSet
)

router = routers.SimpleRouter()
router.register('', AllStatusViewSet)
urlpatterns = router.urls

# urlpatterns = [
#     path('allstatus/', AllStatusViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),
#     # path('predict/', FaultPredictViewSet.as_view({'get': 'list'})),
# ]