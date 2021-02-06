from rest_framework.generics import get_object_or_404
from django.db import models
from ..models import Profile, AvatarImage, WorkImage
from core.models import Skill
from django.utils.timezone import now
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileFollowSerializer, ProfileSerializer, AvatarImageSerializer, WorkImageSerializer
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User


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

        filters = models.Q()
        filters &= models.Q(deactivated_at__isnull=True)

        query_dict = {}

        for k in self.request.query_params.keys():
            query_dict[k] = self.request.query_params.getlist(k)

        for k,vals in query_dict.items():
            if k in ['city','skills','values','q1','q2','q3','state']:
                filters &= models.Q(**{f'{k}__in': vals})
            elif k == 'skillsc':
                for v in vals:
                    filters &= models.Q(skills__in=v)
            elif k == 'valuesc':
                for v in vals:
                    filters &= models.Q(**{k: v})
            elif k == 'bio':
                for v in vals:
                    filters&=models.Q(bio__icontains=v)
            elif k in ["text"]:
                for v in vals:
                    textSkills = Skill.objects.filter(title__icontains = v)
                    filters&=(models.Q(firstname__icontains = v)|models.Q(lastname__icontains = v)| models.Q(skills__in=textSkills))

        queryset = Profile.objects.filter(filters).distinct()
        return queryset

    def get_object(self):
        if self.kwargs.get('pk') == 'me':
            return self.request.user.profile
        return super().get_object()

    def perform_update(self, serializer):
        data = self.request.data
        print("aaaaaaaaaaaaaaaaaaa",self.request.data)        
        serializer.save(last_updated_at = now())

    def perform_destroy(self, instance):
        instance.deactivated_at = now()
        instance.save()


class ProfileFollowerViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = ProfileFollowSerializer
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.filter(deactivated_at__isnull=True)

    def get_object(self):
        if self.kwargs.get('pk') == 'me':
            return self.request.user.profile
        return super().get_object()

class WorkImageViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = WorkImageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):

        if 'uid' in self.request.query_params.keys():
            uid = self.request.query_params.get('uid')
            user = User.objects.get(id=uid)
            queryset = WorkImage.objects.filter(user=user)
        
        return queryset
