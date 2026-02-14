from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Lead, Testimonial


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'status', 'created_at')
    list_filter = ('status', 'service', 'created_at')
    search_fields = ('name', 'email')
    list_editable = ('status',)


from django.contrib import admin
from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    inlines = [ProjectImageInline]

from django.contrib import admin
from .models import Category, BlogPost

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'category', 'published_at')
    list_filter = ('category',)



@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'is_approved', 'created_at')
    list_filter = ('is_approved',)
    list_editable = ('is_approved',)
