import os
from appium.options.android import UiAutomator2Options
from pydantic import BaseModel
from litres_project.utils import file


class Config(BaseModel):
    context: str
    remote_url: str = os.getenv('REMOTE_URL')
    device_name: str = os.getenv('DEVICENAME')
    app_local: str = os.getenv('APP')
    app_bstack: str = os.getenv('APP')
    platformName: str = os.getenv('PLATFORMNAME')
    platformVersion: str = os.getenv('PLATFORMVERSION')
    userName: str = os.getenv('USER_NAME')
    accessKey: str = os.getenv('ACCESS_KEY')
    appWaitActivity: str = "*"
    autoGrantPermissions: bool = True

    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'local':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('platformName', self.platformName)
            options.set_capability('app', file.abs_path_from_project(self.app_local))
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('autoGrantPermissions', self.autoGrantPermissions)

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformName', self.platformName)
            options.set_capability('platformVersion', self.platformVersion)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_bstack)
            options.set_capability('autoGrantPermissions', self.autoGrantPermissions)
            options.set_capability(
                'bstack:options',
                {
                    'projectName': 'First Python project',
                    'buildName': 'browserstack-build-1',
                    'sessionName': 'BStack first_test',
                    'userName': self.userName,
                    'accessKey': self.accessKey,
                },
            )

        return options


config = Config(context="local")
