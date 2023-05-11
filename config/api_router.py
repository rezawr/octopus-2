from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from simpleecom.users.api.views import UserViewSet
from simpleecom.order.api.views import ListCreateSellerView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("sellers", ListCreateSellerView)


app_name = "api"
urlpatterns = router.urls
