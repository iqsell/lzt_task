from database import Database


class DeviceController:
    '''работа с состояниями девайсов'''
    def __init__(self, db_path):
        self.db = Database(db_path)

    def turn_on(self, device_id):
        # включение
        self.db.set_device_state(device_id, 1)

    def turn_off(self, device_id):
        # выключение
        self.db.set_device_state(device_id, 0)

    def get_state(self, device_id):
        # получить состояние
        return self.db.get_device_state(device_id)
