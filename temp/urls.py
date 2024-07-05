from django.urls import path
from temp.views import Blog, Contact, Index, Project

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('project/', Project.as_view(), name='project'),
    path('blog/', Blog.as_view(), name='blog'),
    path('contact/', Contact.as_view(), name='contact'),
]
