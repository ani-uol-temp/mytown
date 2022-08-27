from uuid import UUID

from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from orgs.models import Organisation


@api_view(http_method_names=['GET'])
@permission_classes((permissions.AllowAny,))
def get_public_key(request, pk: UUID):
    return Response(data={
        'publicKey': get_object_or_404(Organisation.objects.all(), pk=pk).public_key
    })
