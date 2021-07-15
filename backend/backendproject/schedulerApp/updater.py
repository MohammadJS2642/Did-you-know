from apscheduler.schedulers .background import BackgroundScheduler
from datetime import datetime
from . import jobs


def starter():
    scheduler = BackgroundScheduler()
    scheduler.add_job(jobs.getter, 'interval', seconds=1440)
    scheduler.start()
