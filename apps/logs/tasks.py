from celery import shared_task

from apps.logs.models import APILog

@shared_task
def save_response_log(response_log):
    api_log = APILog.objects.create(
        log=response_log,
    )

    return f"APILog '{api_log.id}' salvo! - {api_log.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

