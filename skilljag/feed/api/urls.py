from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookMarkViewSet, CommentViewSet, InterestViewSet, PostImageViewSet, PostViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet,basename='posts')
router.register(r"interests", InterestViewSet)
router.register(r"bookmarks", BookMarkViewSet)
router.register(r"comments", CommentViewSet,basename='comments')
router.register(r"images", PostImageViewSet,basename='images')

urlpatterns = [
    path('', include(router.urls)),
]