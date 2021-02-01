from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SkillsViewSet, ValuesViewSet, CitysViewSet, StatesViewSet

router = DefaultRouter()
router.register(r"skills", SkillsViewSet)
router.register(r"values", ValuesViewSet)
router.register(r"citys", CitysViewSet, basename='citys')
router.register(r"states", StatesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]