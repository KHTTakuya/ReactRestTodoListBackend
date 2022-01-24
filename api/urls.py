from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from .views import TodoViewSet, CreateUserView

router = routers.DefaultRouter()
router.register('todo', TodoViewSet)

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('', include(router.urls)),
]
