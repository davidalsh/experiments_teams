from rest_framework_json_api import serializers
from teams import models


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = ('id', 'name')


class ExperimentRetrieveSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(read_only=True, many=True)

    class Meta:
        model = models.Experiment
        fields = ('id', 'description', 'sample_ratio', 'teams', 'teams_count')
        read_only_fields = ('teams_count',)


class ExperimentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experiment
        fields = ('id', 'description', 'sample_ratio', 'teams')

    def create(self, validated_data):
        teams = validated_data.pop('teams')
        instance = self.Meta.model.objects.create(**validated_data, teams_count=len(teams))
        instance.teams.set(teams)
        return instance

    def validate_teams(self, value):
        if not 1 <= len(value) <= 2:
            raise serializers.ValidationError('Please ensure the experiment has exactly 1 or 2 teams assigned.')
        return value
