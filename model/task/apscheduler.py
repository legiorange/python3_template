from apscheduler.schedulers.blocking import BlockingScheduler

print('open')

scheduler = BlockingScheduler()
@scheduler.scheduled_job('interval', seconds=3)
# @scheduler.scheduled_job('cron', id= 'job_0',day_of_week='0-4',hour='6',minute='30')

def job_0():
        print('3秒毎に実行')

print('done')
scheduler.start()