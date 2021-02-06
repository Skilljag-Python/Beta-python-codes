from typing import OrderedDict
from rest_framework.exceptions import ValidationError
from rest_framework.fields import ReadOnlyField
from profiles.api.serializers import UserCompactSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from ..models import BookMark, Comment, Interest, Notification, Post, PostImage


class CommentSerializer(serializers.ModelSerializer):

    created_by = UserCompactSerializer(read_only = True)

    class Meta:

        model = Comment
        fields = [ 'id', 'post', 'text', 'created_by', 'timestamp' ]
        read_only_fields = ['created_by']

class PostImageSerializer(serializers.ModelSerializer):

    class Meta:

        model = PostImage
        fields = [ 'id', 'image']

class ImageSerializer(serializers.ModelSerializer):

    class Meta:

        model = PostImage
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    interest_count = serializers.SerializerMethodField()
    interested = serializers.SerializerMethodField()
    interest_id = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    bookmarked = serializers.SerializerMethodField()
    created_by = UserCompactSerializer(read_only=True)
    comments = CommentSerializer(many = True, read_only = True)
    images = PostImageSerializer(many = True, required = False)

    def get_interest_count(self, post):
        return post.interests.filter(interest='I').count()

    def get_comment_count(self, post):
        return post.comments.filter(deleted_at__isnull = True).count()

    def get_interested(self, post):
        request = self.context.get('request')
        if request:
            user = request.user
            if not user.is_anonymous :  
                try:
                    interest = post.interests.get(created_by = user).interest
                    return interest
                except Interest.DoesNotExist:
                    return 'X'
        return ''

    def get_interest_id(self, post):
        request = self.context.get('request')
        if request:
            user = request.user
            if not user.is_anonymous :  
                try:
                    interest_id = post.interests.get(created_by = user).id
                    return interest_id
                except Interest.DoesNotExist:
                    pass
        return ''

    def get_bookmarked(self, post):
        request = self.context.get("request")
        if request:
            user = request.user
            if not user.is_anonymous :
                try:
                    bookmark =  post.bookmarks.get(created_by = user)
                    return True
                except BookMark.DoesNotExist:
                    pass
        return False

    def validate_images_json(self, value):
        if not isinstance(value, list):
            ValidationError("images expects a list")

        for item in value:
            serializer = PostImageSerializer(data=item)
            serializer.is_valid(raise_exception=True)
        return value
    
    class Meta:

        model = Post
        fields = ['id','interest_count','interested','interest_id','bookmarked','comment_count','created_by', 'category', 'title', 'description', 'timestamp', 'skills','values', 'images', 'comments']


class InterestSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        value = super().to_internal_value(data)
        value['created_by'] = self.context.get("request").user
        return value

    class Meta:
        model = Interest
        fields = '__all__'
        read_only_fields = ['created_by']
        validators = [
            UniqueTogetherValidator(
                queryset=Interest.objects.all(),
                fields=['post', 'created_by']
            )
        ]

class BookMarkSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        value = super().to_internal_value(data)
        value['created_by'] = self.context.get("request").user
        return value

    class Meta:
        model = BookMark
        fields = '__all__'
        read_only_fields = ['created_by']
        validators = [
            UniqueTogetherValidator(
                queryset=BookMark.objects.all(),
                fields=['post', 'created_by']
            )
        ]

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Notification
        fields = '__all__'


