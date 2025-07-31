# logs/handlers.py
import logging
import json

class StructuredLogHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        data = json.loads(log_entry)

        if data.get('event', None) != 'response_log':
            return None

        from apps.logs.tasks import save_response_log
        save_response_log.delay(data)
