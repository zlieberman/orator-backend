from rest_framework import serializers
from .models import Assignment, Book, Classroom, MissedWord, UserAssignment
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'
        

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class UserAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAssignment
        fields = '__all__'


class MissedWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissedWord
        fields = '__all__'