from rest_framework.routers import SimpleRouter, Route

class OptionalSlashRouter(SimpleRouter):
    def __init__(self):
        super().__init__()
        self.trailing_slash = '/?'

class CustomListRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}/{lookup}/?',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={}
        ),
        Route(
            url=r'^{prefix}/?',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={}
        )
    ]

class CustomUpdateRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}$/?',
            mapping={'patch': 'update'},
            name='{basename}-update',
            detail=False,
            initkwargs={}
        )
    ]

class CustomDeleteRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}$/?',
            mapping={'delete': 'destroy'},
            name='{basename}-destroy',
            detail=False,
            initkwargs={}
        )
    ]