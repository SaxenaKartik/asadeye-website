from rest_framework import serializers
from asadeye_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes fields for UserProfile Model"""
    class Meta :
        model = models.UserProfile
        fields = ("id","name","email","phone_no","password")
        extra_kwargs = {
            'password' :{
                'write_only' : True,
                'style' : {'input_type' : 'password'}
            }
        }

    def create(self, validated_data):
        """ Create and return user"""
        user = models.UserProfile.objects.create_user(
            name = validated_data['name'],
            email = validated_data['email'],
            phone_no = validated_data['phone_no'],
            password = validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            instance.set_password(password)
            password = validated_data.pop('password')

        return super().update(instance, validated_data)



class ProductSerializer(serializers.ModelSerializer):
    """Serializes fields for Product Model"""
    class Meta :
        model = models.Products
        fields = ("id","product_name","product_price","product_desc")
        
class ImageSerializer(serializers.ModelSerializer):
    """Serializes fields for Image Model"""
    class Meta :
        model = models.Images
        fields = ("id","image_name", "path", "product_id")
        