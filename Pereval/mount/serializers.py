from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'last_name', 'first_name', 'patronymic', 'phone']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'spring', 'summer', 'autumn']


class ImageSerializer(serializers.ModelSerializer):
    image=serializers.URLField()

    class Meta:
        model = Images
        fields = ['image', 'title']


class PerevalSerializer(serializers.ModelSerializer):
    tourist_id = UserSerializer()
    coord_id = CoordsSerializer()
    level = LevelSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'tourist_id', 'coord_id', 'level', 'images']

    def create(self, validated_data,**kwargs):
        tourist_id=validated_data.pop('tourist_id')
        coord_id=validated_data.pop('coord_id')
        level=validated_data.pop('level')
        images=validated_data.pop('images')

        tourist_id, created=Users.object.get_or_create(**tourist_id)
        coord_id=Coords.objects.create(**coord_id)
        level=Level.objects.create(**level)
        pereval=Pereval.objects.create(**validated_data, tourist_id=tourist_id, coord_id=coord_id,level=level,status="NW")

        for i in images:
            image=i.pop('image')
            title=i.pop('title')
            Images.objects.create(image=image, pereval_id=pereval, title=title)

        return pereval
