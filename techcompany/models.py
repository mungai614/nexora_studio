from django.db import models

# Create your models here.
from django.db import models


class Lead(models.Model):
    SERVICE_CHOICES = [
        ('Web Development', 'Web Development'),
        ('Mobile App Development', 'Mobile App Development'),
        ('Photography', 'Photography'),
        ('Graphic Design', 'Graphic Design'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    message = models.TextField()

    status = models.CharField(
        max_length=50,
        choices=[
            ('New', 'New'),
            ('Contacted', 'Contacted'),
            ('In Progress', 'In Progress'),
            ('Closed', 'Closed'),
        ],
        default='New'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"


from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Web Application', 'Web Application'),
        ('Corporate Website', 'Corporate Website'),
        ('Photography', 'Photography'),
        ('Creative Design', 'Creative Design'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return f"Image for {self.project.title}"

from django.db import models
from django.utils.text import slugify

# Blog Category
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Blog Post
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.excerpt:
            self.excerpt = self.content[:150]  # first 150 chars as preview
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


from django.db import models

class Certification(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=150)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    certificate_file = models.FileField(upload_to='certifications/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.organization}"


import uuid


import uuid
import uuid


import uuid

import uuid
from django.db import models

# models.py
from django.db import models

# models.py
from django.db import models
import uuid

import uuid
from django.db import models

class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    client_image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.PositiveIntegerField(default=5)  # 1-5 stars
    is_approved = models.BooleanField(default=False)
    approval_token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name
