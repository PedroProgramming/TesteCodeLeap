from users.api import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet, basename='post')