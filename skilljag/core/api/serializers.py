
from rest_framework import serializers
from ..models import City, Skill, Value, State


class SkillSerializer(serializers.ModelSerializer):

    class Meta:

        model = Skill
        fields = '__all__'

class ValueSerializer(serializers.ModelSerializer):

    class Meta:

        model = Value
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):

    class Meta:

        model = City
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):

    class Meta:

        model = State
        fields = '__all__'