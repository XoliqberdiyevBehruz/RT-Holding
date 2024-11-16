from django.urls import path

from common import views

urlpatterns = [
    path('settings/', views.SettingsApiView.as_view(), name='settings'),
    path('banner/list/', views.BannerListApiView.as_view(), name='banner-list'),
    path('service/list/', views.ServiceListApiView.as_view(), name='service-list'),
    path('project/list/', views.ProjectListApiView.as_view(), name='project-list'),
    path('project-category/list/', views.ProjectCategoryListApiView.as_view(), name='project-category-list'),
    path('news/list/', views.NewsListApiView.as_view(), name='news-list'),
    path('customer-feedback/list/', views.CustomerFeedbackListApiView.as_view(), name='customer-feedback-list'),
    path('contact-us/create/', views.ContactUsCreateApiView.as_view(), name='contact-us-create'),
    path('product/list/', views.ProductListApiView.as_view(), name='product-list'),
]