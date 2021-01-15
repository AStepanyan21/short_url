from rest_framework import serializers
from .models import URL
import hashlib


def hash_generator(url) -> int:
    url_hash = hashlib.md5(url.encode())
    return url_hash.hexdigest()


class URLSerializer(serializers.Serializer):
    base_url = serializers.CharField(max_length=255)
    short_url = serializers.CharField(max_length=20)

    def create(self, validated_data):
        validated_data['short_url'] = hash_generator(validated_data['short_url'])
        return URL.objects.create(**validated_data)
