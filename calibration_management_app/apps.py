from django.apps import AppConfig


class CalibrationManagementAppConfig(AppConfig):
    name = 'calibration_management_app'

    def ready(self):
    	import calibration_management_app.signals
