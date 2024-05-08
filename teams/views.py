from rest_framework_json_api import views as viewsets

from teams import models
from teams.serializers import ExperimentRetrieveSerializer, ExperimentCreateSerializer, TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all().order_by('-created_at')
    serializer_class = TeamSerializer
    http_method_names = ['get', 'post', 'head', 'options']


class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = models.Experiment.objects.all().order_by('-created_at')
    filterset_fields = ['teams__name']
    http_method_names = ['get', 'post', 'head', 'options']

    def get_serializer_class(self):
        if self.action == 'create':
            return ExperimentCreateSerializer
        return ExperimentRetrieveSerializer
