from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from common.utils import phone_regex

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Settings(BaseModel):
    email = models.EmailField()
    contact_phone_number = models.CharField(max_length=15, validators=[phone_regex])
    contact_phone_number2 = models.CharField(max_length=15, validators=[phone_regex])
    instagram_link = models.URLField()
    facebook_link = models.URLField()
    telegram_link = models.URLField()
    youtube_link = models.URLField()

    def __str__(self):
        return f'Settings RT Holding Company'

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'


class Banner(BaseModel):
    class Type(models.TextChoices):
        home_page = 'Home Page'
        about_us = 'About Us'
        projects = 'Projects'
        news = 'News'
        sale = 'Sale'
        contact_us = 'Contact Us'

    banner = models.ImageField(upload_to='common/banner/banner/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=Type.choices)

    def __str__(self):
        return f'{self.title} - {self.type}'

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'


class Service(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='common/service/images/')
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class ProjectCategory(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Portfolio Category'
        verbose_name_plural = 'Portfolio Categories'


class Project(BaseModel):
    image = models.ImageField(upload_to='common/product/images/')
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='portfolios')
    name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.category.name

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'


class News(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='common/news/images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class CustomerFeedback(BaseModel):
    user_image = models.ImageField(upload_to='common/customer_feedback/user_image/')
    user_role = models.CharField(max_length=100)
    user_full_name = models.CharField(max_length=100)
    user_feedback = models.TextField()
    rate = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.user_full_name} - {self.user_feedback}'

    class Meta:
        verbose_name = 'Customer Feedback'
        verbose_name_plural = 'Customer Feedback'


class UserContactApplication(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, validators=[phone_regex])
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='user_contact_applications')
    text = models.TextField()
    is_contacted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Contact Application'
        verbose_name_plural = 'Contact Application'
        ordering = ['is_contacted']


class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='common/product/images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
