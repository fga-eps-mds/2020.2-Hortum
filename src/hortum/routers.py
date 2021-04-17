from rest_framework.routers import SimpleRouter, Route

class CustomUpdateRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}/?$',
            mapping={'patch': 'update'},
            name='{basename}-update',
            detail=False,
            initkwargs={}
        )
    ]