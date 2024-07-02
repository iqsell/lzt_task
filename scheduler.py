from apscheduler.schedulers.background import BackgroundScheduler
import datetime

from apscheduler.triggers.date import DateTrigger

from database import Database


class TaskScheduler:
    def __init__(self, db_path, device_controller):
        self.db = Database(db_path)
        self.device_controller = device_controller
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self._load_tasks()

    def _load_tasks(self):
        tasks = self.db.get_all_tasks()
        for task in tasks:
            device_id, action, time_str = task
            time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            self._schedule_device_task(device_id, action, time, add_to_db=False)

    def _schedule_device_task(self, device_id, action, time, add_to_db=True):
        if action == "turn_on":
            job = self.scheduler.add_job(lambda: self.device_controller.turn_on(device_id), DateTrigger(run_date=time))
        elif action == "turn_off":
            job = self.scheduler.add_job(lambda: self.device_controller.turn_off(device_id), DateTrigger(run_date=time))

        if add_to_db:
            self.db.save_task(device_id, action, time.strftime("%Y-%m-%d %H:%M:%S"))

    def schedule_task(self, device_id, action, time):
        time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        self._schedule_device_task(device_id, action, time)

    def remove_task(self, job_id):
        self.scheduler.remove_job(job_id)
        self.db.delete_task(job_id)
