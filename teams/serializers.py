from rest_framework_json_api import serializers
from teams import models


class SameFamilyValidation:
    @staticmethod
    def check_family(first_node, second_node):
        if first_node in second_node.get_family():
            raise serializers.ValidationError('Assigned teams cannot belong to the same family.')


class TeamSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = models.Team
        fields = ('id', 'name', 'children', 'parent')
        extra_kwargs = {
            'parent': {'write_only': True},
        }

    def get_children(self, obj):
        children = obj.get_children()
        return TeamSerializer(children, many=True).data


class ExperimentRetrieveSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(read_only=True, many=True)

    class Meta:
        model = models.Experiment
        fields = ('id', 'description', 'sample_ratio', 'teams', 'teams_count')
        read_only_fields = ('teams_count',)


class ExperimentCreateSerializer(serializers.ModelSerializer, SameFamilyValidation):
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
        if len(set(value)) == 2:
            first_team, second_team = value
            self.check_family(first_team, second_team)
        return value


class ExperimentUpdateSerializer(serializers.ModelSerializer, SameFamilyValidation):
    class Meta:
        model = models.Experiment
        fields = ('id', 'teams')

    def validate_teams(self, value):
        if self.instance.teams_count != len(value):
            raise serializers.ValidationError('Please ensure the provided data has the same number of teams '
                                              'as the experiment.')
        if len(set(value)) == 2:
            first_team, second_team = value
            self.check_family(first_team, second_team)
        return value
