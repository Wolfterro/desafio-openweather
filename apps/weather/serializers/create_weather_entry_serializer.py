from rest_framework import serializers

class CreateWeatherEntrySerializer(serializers.Serializer):
    city = serializers.CharField()
    state = serializers.CharField()
    country = serializers.CharField()


class CreateWeatherEntrySerializerError400(serializers.Serializer):
    detail = serializers.CharField()