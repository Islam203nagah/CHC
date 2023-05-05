from django.contrib.auth.models import User
from rest_framework import serializers,validators
from .models import (TbSections,
                     TbSubsections,
                     Category,
                     Articles,
                     Videos,
                     Subtitles,
                     Review)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username", 'password',"email")
        extra_kwargs = {"password": {"write_only": True}}


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "A user with that Email already exists."
                    )
                ],
            }
        }

    def create(self, validated_data):
        user = User(
            email=validated_data.get('email'),
            username=validated_data.get('username'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user










class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model= Articles
        fields= '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model= Category
        fields= '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model= Review
        # fields=('feadback')
        fields= '__all__'


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model= TbSections
        fields= '__all__'



class SubSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model= TbSubsections
        fields= '__all__'


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model= Videos
        fields= ('id','video_name','category','video_path')



class SubtitlesSerializer(serializers.ModelSerializer):

    class Meta:
        model= Subtitles
        fields= '__all__'
        


