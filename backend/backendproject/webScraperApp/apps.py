from django.apps import AppConfig


class WebscraperappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webScraperApp'

    def ready(self):
        from schedulerApp import updater
        updater.starter()
