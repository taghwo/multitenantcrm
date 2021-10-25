from celery.decorators import periodic_task
from celery.schedules import crontab

@periodic_task(
    run_every=(crontab(days='*/15')),
    name="delete_dormant_accounts",
    ignore_result=True
)
def delete_dormant_accounts():
    pass
