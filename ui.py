class SmartHomeUI:
    def __init__(self, device_controller, scheduler, weather_service):
        self.device_controller = device_controller
        self.scheduler = scheduler
        self.weather_service = weather_service

    def run(self):
        while True:
            command = input("Введите команду (turn_on, turn_off, schedule, weather, exit): ")
            if command == "exit":
                break
            elif command == "turn_on":
                device_id = int(input("Введите ID девайса: "))
                self.device_controller.turn_on(device_id)
            elif command == "turn_off":
                device_id = int(input("Введите ID девайса: "))
                self.device_controller.turn_off(device_id)
            elif command == "schedule":
                device_id = int(input("Введите ID девайса: "))
                action = input("Выберите действие (turn_on/turn_off): ").strip().lower()
                time = input("Введите время (YYYY-MM-DD HH:MM:SS): ").strip()
                self.scheduler.schedule_task(device_id, action, time)
            elif command == "weather":
                location = input("Введите город(Напр.: London): ")
                weather = self.weather_service.get_weather(location)
                print(weather)
