from celery import shared_task

@shared_task
def print_message(message):
    print(message)
    return message
