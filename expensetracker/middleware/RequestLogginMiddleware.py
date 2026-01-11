
from tracker.models import RequestLogs
import json

class RequestLogging:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Log request BEFORE response
        RequestLogs.objects.create(
            request_info=json.dumps({
                "path": request.path,
                "method": request.method,
                "ip": request.META.get("REMOTE_ADDR"),
                "user": request.user.username if request.user.is_authenticated else "Anonymous",
            }),
            request_type=request.method,
            request_method=request.path
        )

        response = self.get_response(request)   # CALL ONCE

        return response
