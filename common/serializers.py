from rest_framework import serializers

from common import models


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Settings
        fields = [
            'id', 'email', 'contact_phone_number', 'contact_phone_number2',
            'instagram_link', 'telegram_link', 'facebook_link', 'youtube_link'
        ]


class BannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = [
            'id', 'title', 'description', 'banner',
        ]


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = [
            'id', 'title', 'description', 'image',
        ]


class ProjectCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectCategory
        fields = [
            'id', 'name'
        ]


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = [
            'id', 'name', 'image', 'link', 'category'
        ]


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = [
            'id', 'title', 'description', 'image',
        ]


class CustomerFeedbackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerFeedback
        fields = [
            'id', 'user_full_name', 'user_feedback', 'user_image', 'user_role', 'rate',
        ]


class UserContactApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserContactApplication
        fields = [
            'name', 'email', 'phone_number', 'service', 'text'
        ]


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = [
            'id', 'name', 'description', 'image'
        ]