from django.contrib.auth import models
from core.api.serializers import CitySerializer, SkillSerializer, ValueSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Profile, AvatarImage
from core.models import Skill, Value

class UserCompactSerializer(serializers.ModelSerializer):

    avatar = serializers.ImageField(source='avatar.avatar', read_only = True)
    firstname = serializers.CharField(source='profile.firstname', read_only=True)
    lastname = serializers.CharField(source='profile.lastname', read_only=True)
    company = serializers.CharField(source='profile.company', read_only=True)

    def get_avatar(self, user):
        avatar = user.profile.avatar
        if avatar != "":
            return avatar.url
        return ""

    class Meta:

        model = User
        fields = ['id', 'avatar', 'firstname', 'lastname','company']

class AvatarImageSerializer(serializers.ModelSerializer):

    class Meta:

        model = AvatarImage
        fields = [ 'id', 'avatar', 'user']

class ProfileSerializer(serializers.ModelSerializer):

    email = serializers.CharField(source='user.email', read_only=True)
    #skills = SkillSerializer(many = True,required= False, read_only=True)
    #values = ValueSerializer(many = True,required = False)
    #following = UserCompactSerializer(many=True, required = False, read_only = True)
    following_count = serializers.SerializerMethodField()
    followers = UserCompactSerializer(many = True, required=False)
    followers_count = serializers.SerializerMethodField()
    avatar = serializers.ImageField(source='user.avatar.avatar', read_only = True)
    me_following = serializers.SerializerMethodField()

    def get_following_count(self, profile):
        return profile.following.filter(profile__deactivated_at__isnull=True).count()

    def get_followers_count(self, profile):
        return User.objects.filter(profile__following__id__contains=profile.user.id).count()

    def get_me_following(self, profile):
        if(self.context.get('request').user.profile.following.filter(id=profile.id).exists()):
            return True
        else:
            return False

    def update(self, instance, validated_data):
        skills_data = []
        values_data = []
        print("@@@@@@@@@@@@@",validated_data.values())
        if('skills' in validated_data.keys()):
            skills_data = validated_data.pop('skills')
            print("***************",skills_data)
        if('values' in validated_data.keys()):
            values_data = validated_data.pop('values')
            print("################",values_data)
        instance = super().update(instance, validated_data)
        if(len(skills_data)>0):
            instance.skills.set([])
            for skill_data in skills_data:
                nskills = Skill.objects.filter(id=skill_data.id)
                if(nskills.exists()):
                    nskill = nskills.first()
                    instance.skills.add(nskill)

        if(len(values_data)>0):
            instance.values.set([])
            for value_data in values_data:
                nvalues = Value.objects.filter(id=value_data.id)
                if(nvalues.exists()):
                    nvalue = nvalues.first()
                    instance.values.add(nvalue)

        return instance

    """ def update(self, instance, validated_data):
        skills = validated_data.pop('skills', [])
        instance = super().update(instance, validated_data)
        for skill_data in skills:
            skill = Skill.objects.get(title=skill_data.get('title'))
            instance.skills.add(skill)
        values = validated_data.pop('values', [])
        instance = super().update(instance, validated_data)
        for value_data in values:
            value = Value.objects.get(title=value_data.get('title'))
            instance.values.add(value)
        return instance  """

    class Meta:
        model = Profile
        fields = ['me_following','id','firstname','lastname','email','gender','birthdate','bio','phone','city','languages','skills','values','q1','q2','q3','pic','highested','designation','tandcversion','avatar','completed_at','followers', 'following', 'followers_count', 'following_count','institution','state', 'company']


class ProfileFollowSerializer(serializers.ModelSerializer):

    following = UserCompactSerializer(many = True, required=False)

    class Meta:
        model = Profile
        fields = ['id','following']