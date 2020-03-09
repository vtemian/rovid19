from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from cases.models import Cases
from .serializers import CasesSerializer


class CasesViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Cases.objects.all().order_by('-created_at')
    serializer_class = CasesSerializer
