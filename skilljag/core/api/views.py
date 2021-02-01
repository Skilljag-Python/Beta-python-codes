from core.models import Skill, City, Value, State
from rest_framework import viewsets, mixins
from .serializers import CitySerializer, SkillSerializer, ValueSerializer, StateSerializer


class SkillsViewSet(mixins.RetrieveModelMixin, 
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = SkillSerializer
    queryset = Skill.objects.all()
    pagination_class = None

class ValuesViewSet(mixins.RetrieveModelMixin, 
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = ValueSerializer
    queryset = Value.objects.all()
    pagination_class = None

class CitysViewSet(mixins.RetrieveModelMixin, 
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = CitySerializer
    pagination_class = None

    def get_queryset(self):
        query_dict = {}
        for k in self.request.query_params.keys():
            query_dict[k] = self.request.query_params.getlist(k)

        if 'state' in query_dict.keys():
            state = query_dict.get('state')[0]
            queryset = City.objects.filter(state=state)
        else:
            queryset = City.objects.all()

        return queryset

class StatesViewSet(mixins.RetrieveModelMixin, 
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = StateSerializer
    queryset = State.objects.all()
    pagination_class = None