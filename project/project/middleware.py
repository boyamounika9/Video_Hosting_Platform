import logging
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponseBadRequest, JsonResponse

logger = logging.getLogger(__name__)

class Catch400Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, SuspiciousOperation):
            logger.error(f"400 ERROR CAUGHT: {type(exception).__name__} - {str(exception)}")
            is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
            msg = f"Upload Error ({type(exception).__name__}): {str(exception)}"
            if is_ajax:
                return JsonResponse({'status': 'error', 'message': msg}, status=400)
            return HttpResponseBadRequest(
                f"<html><body><h1>Bad Request Diagnostics</h1>"
                f"<h2>Type: {type(exception).__name__}</h2>"
                f"<p>Message: {str(exception)}</p></body></html>"
            )
        return None
