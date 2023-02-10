"""
Views for nexus_drf
"""
# Imports
# -----------------------------------------------------------------------
# Third Party
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        'message': 'Welcome to the Nexus Django REST Framework API.'
    })
