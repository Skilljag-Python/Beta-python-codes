
from typing import OrderedDict
from django.db.models.aggregates import Count, Sum
from django.db.models.expressions import Case, ExpressionWrapper, F, Value, When
from django.db.models.fields import IntegerField
from django.utils.timezone import now
from django.db import models

from rest_framework import generics, status, viewsets, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import BookMark, Comment, Interest, Post, PostImage
from .serializers import BookMarkSerializer, CommentSerializer, ImageSerializer, InterestSerializer, PostImageSerializer, PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    #queryset = Post.objects.filter(deleted_at__isnull = True).order_by("-timestamp")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        
        filters = models.Q()
        filters &= models.Q(deleted_at__isnull=True)

        query_dict = {}

        for k in self.request.query_params.keys():
            query_dict[k] = self.request.query_params.getlist(k)

        if 'recommended' in query_dict.keys():
            para = query_dict.get('recommended')[0]
            user = self.request.user
            skills = user.profile.skills.all()
            skill1 = skills[0].id
            skill2 = skills[1].id
            skill3 = skills[2].id
            skill4 = skills[3].id
            """ filters&= models.Q(skills__in=skills) """
            queryset = Post.objects.filter(filters).distinct()
            #queryset = queryset.annotate(skill1_c=Case(When(skills__in=skill1,then = Value(1)),default=Value(0),output_field=IntegerField()))
            queryset = queryset.annotate(When(skills__id = skill1,then = 1))
            for item in queryset:
                print(str(item))

            print('hai')
            #queryset = queryset.annotate(skill2_c=Case(When(skills__in=skill2,then = Value('1',IntegerField())),default=Value('0',IntegerField())))
            #queryset = queryset.annotate(skill3_c=Case(When(skills__in=skill3,then = Value('1',IntegerField())),default=Value('0',IntegerField())))
            #queryset = queryset.annotate(skill4_c=Case(When(skills__in=skill4,then = Value('1',IntegerField())),default=Value('0',IntegerField())))
            #queryset = queryset.annotate(tot=ExpressionWrapper(F('skill1_c')+F('skill2_c')+F('skill3_c')+F('skill4_c'),output_field=IntegerField())).order_by('-tot')
            for item in queryset:
                print(item)
                #print(item,' ',item.skill1_c,' ',item.skill2_c,' ',item.skill3_c,' ',item.skill3_c,' ',item.tot)
        else:
            for k,vals in query_dict.items():
                if k in ['category','skills','values','created_by']:
                    filters &= models.Q(**{f'{k}__in': vals})
                elif k =='uid':
                    filters &= models.Q(created_by__id__in = vals)
                elif k in ['followers']:
                    filters &= models.Q(created_by__follows__to_user_id__in = vals)
                elif k in ['followersc']:
                    for v in vals:
                        filters &= models.Q(created_by__follows__to_user_id__in = v)
                elif k in ['follows']:
                    filters &= models.Q(created_by__followers__from_user_id__in = vals)
                elif k in ['followsc']:
                    for v in vals:
                        filters &= models.Q(created_by__followers__from_user_id__in = v)
                elif k in ['interested']:
                    filters &= models.Q(interests__created_by__id__in = vals)
                elif k in ['interestedc']:
                    for v in vals:
                        filters &= models.Q(interests__created_by__id__in = v)
                elif k in 'skillsc':
                    for v in vals:
                        filters &= models.Q(skills__in=v)
                elif k in 'valuesc':
                    for v in vals:
                        filters &= models.Q(**{k: v})
                elif k == 'text':
                    for v in vals:
                        filters&=( models.Q(title__icontains=v) | models.Q(description__icontains=v))
                elif k in ["name"]:
                    for v in vals:
                        filters&=(models.Q(created_by__username__icontains = v) | models.Q(created_by__first_name__icontains = v)|models.Q(created_by__last_name__icontains = v))
                        
            queryset = Post.objects.filter(filters)
            if 'ordering' in query_dict.keys():
                para = query_dict.get('ordering')[0]
                if para == 'recent':
                    queryset = queryset.order_by('-timestamp')
                elif para == 'trending':
                    queryset = queryset.annotate(interest_count=Count('interests')).order_by('-interest_count')
        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted_at = now()
        instance.save()


class InterestViewSet(mixins.CreateModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    queryset = Interest.objects.filter(post__deleted_at__isnull = True)
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]

class BookMarkViewSet(mixins.CreateModelMixin, 
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    queryset = BookMark.objects.filter(post__deleted_at__isnull = True)
    serializer_class = BookMarkSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CommentViewSet(mixins.CreateModelMixin, 
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

    #queryset = Comment.objects.filter(deleted_at__isnull = True)
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        queryset = Comment.objects.filter(deleted_at__isnull = True, post__deleted_at__isnull = True)
        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted_at = now()
        instance.save()

class PostImageViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]