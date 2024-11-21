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
    instagram_link = models.URLField()
    facebook_link = models.URLField()
    telegram_link = models.URLField()
    youtube_link = models.URLField()

    def __str__(self):
        return f'Settings RT Holding Company'

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'


class ContactPhoneNumber(BaseModel):
    phone_number = models.CharField(max_length=15, validators=[phone_regex])
    settings = models.ForeignKey(Settings, on_delete=models.CASCADE, related_name='contact_phone_numbers')

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Contact Phone Number'
        verbose_name_plural = 'Contact Phone Number'


class Banner(BaseModel):
    class Type(models.TextChoices):
        home_page = 'Home Page'
        about_us = 'About Us'
        projects = 'Projects'
        news = 'News'
        sale = 'Sale'
        contact_us = 'Contact Us'
        our_services = 'Our Services'

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


class Project(BaseModel):
    image = models.ImageField(upload_to='common/product/images/')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='portfolios')
    name = models.CharField(max_length=100)
    link = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.service.title}'

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'


class ProjectBanner(BaseModel):
    banner = models.ImageField(upload_to='common/project/banner/images/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project Banner'
        verbose_name_plural = 'Project Banner'
        unique_together = (('project', 'title'),)

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
    main_image = models.ImageField(upload_to='common/product/main-image/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductMedia(BaseModel):
    image = models.ImageField(upload_to='common/product-media/images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_media')


class OurInfo(BaseModel):
    title = models.CharField(max_length=100)
    text = models.TextField()
    banner = models.ImageField(upload_to='common/product/banner/images/')
    image1 = models.ImageField(upload_to='common/product/images/')
    image2 = models.ImageField(upload_to='common/product/images/')
    image3 = models.ImageField(upload_to='common/product/images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Our Info'
        verbose_name_plural = 'Our Info'


class InfoCompany(BaseModel):
    image = models.ImageField(upload_to='common/info-company/images/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_count = models.PositiveBigIntegerField(default=0)
    customers_count = models.PositiveBigIntegerField(default=0)
    grateful_customers_count = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Info Company'
        verbose_name_plural = 'Info Company'
