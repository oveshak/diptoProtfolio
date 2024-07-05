from django.shortcuts import redirect
from django.views.generic.base import TemplateView

from contacts.models import ContactUs, SocalMedia

from globals.models import Global
from project.models import Projects
from blogs.models import Blogs
from home.models import HeroItem
# Create your views here.
class Mixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] =Projects.objects.first()
        context['blog'] = Blogs.objects.first()
        context['global'] = Global.objects.first()
        return context
    
    def post(self,request,*args, **kwargs):
        name=request.POST.get('contact_name')
        email=request.POST.get('contact_email')
        message=request.POST.get('contact_message')
        ContactUs.objects.create(
            name=name,
            email=email,
            message=message

        )
        return redirect('index')
    
    
class Index(Mixin,TemplateView):
    template_name = "temp/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hero'] =HeroItem.objects.first()
        return context

class Project(Mixin,TemplateView):
    template_name = "temp/projects.html"

class Blog(Mixin,TemplateView):
    template_name = "temp/blogs.html"

class Contact(Mixin,TemplateView):
    template_name = "temp/contact.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['socal'] = SocalMedia.objects.all()
        return context

    