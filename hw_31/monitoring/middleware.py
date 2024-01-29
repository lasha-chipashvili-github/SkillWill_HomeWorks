import logging
from rest_framework.status import is_success


class PostsMonitoringMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger()


    def __call__(self, request):
        try:
            self.process_request(request)
            response = self.get_response(request)
            response = self.process_response(request, response)

            if is_success():
                self._log_successful_request(request, response)

            return response
        except Exception as exc:
            self.logger.error(exc)
            return self.get_response(request)


    def process_request(self, request):
        self._log_message(f"[process_request] => request: {request}")

    def process_response(self, response):
        self._log_message(f"[process_request] => response: {response}")
        return response


    def _log_message(self, message):
        self.logger.ingo(f"[{self.__class__.__name__}.Monitoring {message}]")

    def _log_successful_request(self, request, response):
        self.logger.info(f"[{self.__class__.__name__}.Monitoring Middleware] [successful_request]=>",
                         f"{request.method}, {request.path} - {response.status_code}")

