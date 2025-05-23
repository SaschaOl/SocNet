from django.shortcuts import render
from django.views.generic.edit import BaseFormView
from django.views.generic.list import ListView
from django.views.generic.base import View
from .forms import PostForm, PostDeletionForm
from .models import Post, PostImage
from user_app.models import SocNetUser
from django.urls import reverse_lazy
# from django.contrib.auth.views import 

# Create your views here.

class PostCreationView(BaseFormView):
    form_class = PostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form: PostForm):
        print(form.cleaned_data)
        data = form.cleaned_data
        new_post = Post.objects.create(
            author = SocNetUser.objects.get(id = self.request.user.id),
            title = data['title'],
            # tags = data['tags'],
            post_text = data['post_text']
        )
        new_post.tags.set(data['tags'])
        for image in data['images']:
            PostImage.objects.create(
                post = new_post,
                file = image
            )
        return super().form_valid(form)


class MyPostsView(ListView):
    model = Post
    template_name = 'my_posts.html'
    extra_context = {'deletion_form': PostDeletionForm}


class PostDeletionView(BaseFormView):
    form_class = PostDeletionForm
    success_url = reverse_lazy('my_posts')

    def form_valid(self, form: PostDeletionForm):
        delete_post_id = form.cleaned_data['post_id']
        Post.objects.get(id= delete_post_id).delete()
        return super().form_valid(form)