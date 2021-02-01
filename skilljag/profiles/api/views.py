from rest_framework.generics import get_object_or_404
from ..models import Profile, AvatarImage
from django.utils.timezone import now
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer, AvatarImageSerializer
from .permissions import IsOwnerOrReadOnly

class AvatarImageViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = AvatarImageSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        AvatarImage.objects.filter(user=self.request.user).delete()
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):

        queryset = AvatarImage.objects.filter(user__profile__deactivated_at__isnull=True)
        return queryset

    def get_object(self):
        if self.kwargs.get('pk') == 'me':
            return self.request.user.avatar
        return super().get_object()

class ProfileViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):

        queryset = Profile.objects.filter(deactivated_at__isnull=True)
        return queryset

    def get_object(self):
        if self.kwargs.get('pk') == 'me':
            return self.request.user.profile
        return super().get_object()

    def perform_update(self, serializer):
        serializer.save(last_updated_at = now())

    def perform_destroy(self, instance):
        instance.deactivated_at = now()
        instance.save()
