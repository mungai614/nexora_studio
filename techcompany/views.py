from django.core.mail import send_mail
from django.shortcuts import render

from technology import settings


# Create your views here.
def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')


from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from .models import Lead


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        message = request.POST.get('message')

        # Save to database
        lead = Lead.objects.create(
            name=name,
            email=email,
            service=service,
            message=message
        )

        # -------- EMAIL TO YOU --------
        subject = f"New Project Inquiry from {name}"
        html_content = f"""
        <h2>New Lead Received</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Service:</strong> {service}</p>
        <hr>
        <p><strong>Message:</strong></p>
        <p>{message}</p>
        """

        msg = EmailMultiAlternatives(
            subject,
            "",
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        # -------- AUTO CONFIRMATION TO CLIENT --------
        client_subject = "We've Received Your Project Inquiry 🚀"

        client_html = f"""
        <h2>Hello {name},</h2>
        <p>Thank you for reaching out to Nexora Studios.</p>
        <p>We have received your inquiry regarding <strong>{service}</strong>.</p>
        <p>Our team will get back to you within 24 hours.</p>
        <br>
        <p>Best regards,<br>Nexora Studios</p>
        """

        client_msg = EmailMultiAlternatives(
            client_subject,
            "",
            settings.EMAIL_HOST_USER,
            [email],
        )
        client_msg.attach_alternative(client_html, "text/html")
        client_msg.send()

        messages.success(request, "Your inquiry has been sent successfully!")

    return render(request, 'contact.html')


from .models import Project


from .models import Project

def portfolio(request):
    projects = Project.objects.prefetch_related('images').all()
    return render(request, 'portfolio.html', {'projects': projects})



def portfolio_category(request, category):
    projects = Project.objects.filter(category=category)
    return render(request, 'portfolio_category.html', {
        'projects': projects,
        'category': category
    })

def why_choose_us(request):
    return render(request, 'why_choose_us.html')

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost, Category

from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category
from django.core.paginator import Paginator

# Blog List Page
def blog_list(request):
    category_slug = request.GET.get('category')
    categories = Category.objects.all()
    posts = BlogPost.objects.all().order_by('-published_at')

    if category_slug:
        posts = posts.filter(category__slug=category_slug)

    paginator = Paginator(posts, 6)  # 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog_list.html', {
        'categories': categories,
        'page_obj': page_obj,
        'selected_category': category_slug
    })

# Blog Detail Page
def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_detail.html', {'post': post})


from .models import Certification

def certifications(request):
    all_certs = Certification.objects.all().order_by('-issue_date')
    return render(request, 'certifications.html', {'certifications': all_certs})


from .models import Testimonial

from django.db.models import Avg

from django.db.models import Avg

from techcompany.models import Testimonial
import uuid
from django.shortcuts import render

def testimonials(request):
    valid_testimonials = []

    for t in Testimonial.objects.all():
        try:
            uuid.UUID(str(t.approval_token))  # only keep valid UUIDs
            valid_testimonials.append(t)
        except (ValueError, TypeError):
            pass  # skip this testimonial entirely

    return render(request, 'testimonials.html', {
        'testimonials': valid_testimonials
    })

# views.py
from django.shortcuts import render, redirect
from .forms import TestimonialForm

from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings

def add_testimonial(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save()

            approval_link = request.build_absolute_uri(
                reverse('approve_testimonial', args=[testimonial.approval_token])
            )

            send_mail(
                subject="New Testimonial Pending Approval",
                message=f"""
A new testimonial was submitted.

Client: {testimonial.client_name}
Company: {testimonial.company}
Rating: {testimonial.rating}

Approve here:
{approval_link}
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["your@email.com"],
            )

            return redirect('testimonials')
    else:
        form = TestimonialForm()

    return render(request, 'add_testimonial.html', {'form': form})


from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect

@staff_member_required
def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    testimonial.delete()
    return redirect('testimonials')

from django.shortcuts import get_object_or_404, redirect
from .models import Testimonial

def approve_testimonial(request, token):
    testimonial = get_object_or_404(Testimonial, approval_token=token)
    testimonial.is_approved = True
    testimonial.save()
    return redirect('testimonials')

