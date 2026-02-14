
from django.contrib import admin
from django.urls import path

from techcompany import views
from django.conf import settings
from django.conf.urls.static import static

from techcompany.views import add_testimonial

urlpatterns = [
path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # ← homepage at root
    path('home/', views.home),          # optional, if you want /home too
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/<str:category>/', views.portfolio_category, name='portfolio_category'),
    path('why-choose-us/', views.why_choose_us, name='why_choose_us'),
    path('certifications/', views.certifications, name='certifications'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
path('testimonials/add/', add_testimonial, name='add_testimonial'),
path('testimonials/delete/<int:pk>/', views.delete_testimonial, name='delete_testimonial'),
path('approve-testimonial/<uuid:token>/', views.approve_testimonial, name='approve_testimonial'),

              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
