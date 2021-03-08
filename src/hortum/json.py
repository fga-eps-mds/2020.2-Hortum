from rest_framework.renderers import JSONRenderer
from rest_framework import serializers

class SerializedToJson:

    def toJson(serialized):
        return JSONRenderer().render(serialized.data)

