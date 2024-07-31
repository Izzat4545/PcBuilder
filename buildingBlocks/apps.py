from django.apps import AppConfig

class BuildingBlocksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'buildingBlocks'
    
    def ready(self):
        import buildingBlocks.signals
