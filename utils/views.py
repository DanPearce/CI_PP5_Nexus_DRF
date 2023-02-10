"""
Views for utils
"""
# Imports
# -----------------------------------------------------------------------
# Third Party
from django.http import JsonResponse


def HTTP_404(request, exception):
    """
    404 HTTP Status Code response in JSON
    """
    message = ('Sorry! Looks like this page does not exist.')

    response = JsonResponse(data={
        'message': message,
        'status_code': 404
    })
    response.status_code = 404
    return response
