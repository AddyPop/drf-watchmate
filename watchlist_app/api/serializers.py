from rest_framework import serializers
from watchlist_app.models import watchlist, streamplatform, review

class watchlistSerializers(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    def get_len_name(self, object):
        return len(object.title)

    class Meta:
        model = watchlist
        fields = '__all__'


class reviewSerializers(serializers.ModelSerializer):
    reviews = watchlistSerializers(many=True, read_only=True)

    class Meta:
        model = review
        exclude = ('watchlist',)
        #fields = '__all__'


class streamplatformSerializers(serializers.ModelSerializer):
    watchlist = watchlistSerializers(many=True, read_only=True)
    class Meta:
        model = streamplatform
        fields = '__all__'

"""
def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short to save.")

class MovieSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name= validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and Description can not be same, Please change..!")
        return data
        """