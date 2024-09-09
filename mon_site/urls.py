from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include(router.urls)),
    path("auth/", include("auth_api.urls")),
]
