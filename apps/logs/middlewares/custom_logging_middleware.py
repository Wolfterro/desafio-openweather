import json
import structlog
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest

logger = structlog.get_logger("custom_logging")

class CustomLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        request._body = request.body

    def process_response(self, request: HttpRequest, response):
        body = request._body.decode('utf-8', errors='ignore')
        response_body = getattr(response, 'content', b'').decode('utf-8', errors='ignore')
        logger.info(
            "response_log",
            url=request.build_absolute_uri(),
            method=request.method,
            headers=json.loads(json.dumps({k: v for k, v in request.headers.items()})),
            body=json.loads(body) if body else None,
            status=response.status_code,
            response=json.loads(response_body) if response_body else None,
            user=str(getattr(request, 'user', None)),
        )

        return response
