import config
from ui import SmartHomeUI
from device_controller import DeviceController
from scheduler import TaskScheduler
from weather_service import WeatherService

def main():
    device_controller = DeviceController(config.DB_PATH)
    scheduler = TaskScheduler(config.DB_PATH, device_controller)
    weather_service = WeatherService(api_key=config.WEATHER_API_KEY)

    ui = SmartHomeUI(device_controller, scheduler, weather_service)
    ui.run()

if __name__ == "__main__":
    main()
