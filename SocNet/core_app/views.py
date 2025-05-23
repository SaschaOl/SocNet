from django.shortcuts import render
from django.views.generic import TemplateView
from post_app.forms import PostForm
from post_app.models import Post
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'form': PostForm,
        'post_list': Post.objects.all()
    }
