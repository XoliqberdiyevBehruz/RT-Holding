from rest_framework import generics, views, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from common import models, serializers


class SettingsApiView(views.APIView):
    def get(self, request):
        settings = models.Settings.objects.all().first()
        serializer = serializers.SettingsSerializer(settings)
        return Response(serializer.data)


class BannerListApiView(views.APIView):
    def get(self, request):
        banners = models.Banner.objects.all()
        serializer = serializers.BannerListSerializer(banners, many=True)
        return Response(serializer.data)


class ServiceListApiView(views.APIView):
    def get(self, request):
        services = models.Service.objects.all()
        serializer = serializers.ServiceListSerializer(services, many=True)
        return Response(serializer.data)


class ProjectCategoryListApiView(views.APIView):
    def get(self, request):
        categories = models.ProjectCategory.objects.all()
        serializer = serializers.ProjectCategoryListSerializer(categories, many=True)
        return Response(serializer.data)


class ProjectListApiView(views.APIView):
    def get(self, request):
        projects = models.Project.objects.all()
        serializer = serializers.ProjectListSerializer(projects, many=True)
        return Response(serializer.data)


class NewsListApiView(views.APIView):
    def get(self, request):
        news = models.News.objects.all()
        serializer = serializers.NewsListSerializer(news, many=True)
        return Response(serializer.data)


class CustomerFeedbackListApiView(views.APIView):
    def get(self, request):
        feedbacks = models.CustomerFeedback.objects.all()
        serializer = serializers.CustomerFeedbackListSerializer(feedbacks, many=True)
        return Response(serializer.data)


class ContactUsCreateApiView(generics.CreateAPIView):
    queryset = models.UserContactApplication
    serializer_class = serializers.UserContactApplicationCreateSerializer
    parser_classes = (MultiPartParser, FormParser)


class ProductListApiView(views.APIView):
    def get(self, request):
        products = models.Product.objects.all()
        serializer = serializers.ProductListSerializer(products, many=True)
        return Response(serializer.data)
