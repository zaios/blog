from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.Serializer):
    name= serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    job_title = serializers.CharField()
    created_time =  serializers.DateTimeField()
  
    def create(self, validated_data):
        print(validated_data)
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.job_title = validated_data.get('job_title', instance.job_title)
        # instance.created_time = validated_data.get('view', instance.created_time)
       
        instance.save()
        return instance