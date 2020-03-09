from rest_framework import serializers

from cases.models import Cases


class CasesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cases
        fields = ['created_at', 'no_confirmed', 'no_special_quarantined', 'no_self_quarantined', 'no_recovered',
                  'global_no_confirmed', 'global_no_deaths', 'global_no_recovered', ]