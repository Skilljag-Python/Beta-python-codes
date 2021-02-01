from core.api.serializers import CitySerializer, SkillSerializer, ValueSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Profile, AvatarImage

class UserCompactSerializer(serializers.ModelSerializer):

    avatar = serializers.ImageField(source='avatar.avatar', read_only = True)
    firstname = serializers.CharField(source='profile.firstname', read_only=True)
    lastname = serializers.CharField(source='profile.lastname', read_only=True)

    def get_avatar(self, user):
        avatar = user.profile.avatar
        if avatar != "":
            return avatar.url
        return ""

    class Meta:

        model = User
        fields = ['id', 'avatar', 'firstname', 'lastname']

class AvatarImageSerializer(serializers.ModelSerializer):

    class Meta:

        model = AvatarImage
        fields = [ 'id', 'avatar', 'user']

class ProfileSerializer(serializers.ModelSerializer):

    email = serializers.CharField(source='user.email', read_only=True)
    skills = SkillSerializer(many = True,required= False)
    values = ValueSerializer(many = True,required = False)
    following = UserCompactSerializer(many=True, required = False)
    following_count = serializers.SerializerMethodField()
    followers = UserCompactSerializer(many = True, required=False)
    followers_count = serializers.SerializerMethodField()
    avatar = serializers.ImageField(source='user.avatar.avatar', read_only = True)

    def get_following_count(self, profile):
        return profile.following.filter(profile__deactivated_at__isnull=True).count()

    def get_followers_count(self, profile):
        return User.objects.filter(profile__following__id__contains=profile.user.id).count()

    class Meta:
        model = Profile
        fields = ['id','firstname','lastname','email','gender','birthdate','bio','phone','city','languages','skills','values','q1','q2','q3','pic','highested','designation','tandcversion','avatar','completed_at','followers', 'following', 'followers_count', 'following_count','institution','state', 'company']
