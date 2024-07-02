import sqlite3


class Database:
    '''Создание бд'''

    def __init__(self, db_path):
        self.db_path = db_path
        self._create_tables()

    def _create_tables(self):
        with self._get_connection() as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS devices (id INTEGER PRIMARY KEY, name TEXT, state INTEGER)"
            )
            conn.execute(
                "CREATE TABLE IF NOT EXISTS schedule (id INTEGER PRIMARY KEY, device_id INTEGER, action TEXT, time TEXT)"
            )
            conn.execute("INSERT INTO devices (name, state) VALUES ('Телевизор', 1), ('Кондиционер', 0)")
            conn.execute("INSERT INTO schedule (device_id, action, time) VALUES "
                         "(1, 'turn_on', '2024-07-02 14:30:00'),"
                         "(2, 'turn_off', '2024-07-02 20:00:00')")

    def _get_connection(self):
        return sqlite3.connect(self.db_path, check_same_thread=False)

    ''' запросы к бд '''

    def get_device_state(self, device_id):
        conn = self._get_connection()
        result = conn.execute("SELECT state FROM devices WHERE id = ?", (device_id,))
        return result.fetchone()

    def set_device_state(self, device_id, state):
        conn = self._get_connection()
        with conn:
            conn.execute("UPDATE devices SET state = ? WHERE id = ?", (state, device_id))

    def get_all_tasks(self):
        conn = self._get_connection()
        result = conn.execute("SELECT device_id, action, time FROM schedule")
        return result.fetchall()

    def save_task(self, device_id, action, time):
        conn = self._get_connection()
        with conn:
            conn.execute("INSERT INTO schedule (device_id, action, time) VALUES (?, ?, ?)",
                         (device_id, action, time))

    def delete_task(self, job_id):
        conn = self._get_connection()
        with conn:
            conn.execute("DELETE FROM schedule WHERE id = ?", (job_id,))
