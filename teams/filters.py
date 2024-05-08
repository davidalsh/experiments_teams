import django_filters
from django_filters import rest_framework as filters
from teams.models import Experiment


class TeamNameFilterBackend(filters.FilterSet):
    team_name = django_filters.CharFilter(field_name='team_name', method='filter_children')

    class Meta:
        model = Experiment
        fields = ('team_name',)

    @staticmethod
    def filter_children(queryset, _, value):
        ids_exclude = []
        for obj in queryset:
            for team in obj.teams.all():
                if value.lower() not in team.name.lower() and not team.get_descendants().filter(name__icontains=value):
                    ids_exclude.append(obj.id)
        return queryset.exclude(id__in=ids_exclude)
