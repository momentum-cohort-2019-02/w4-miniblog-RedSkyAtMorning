from django.shortcuts import render
from blog.models import Blogger, Post

def index(request):
    num_bloggers = Blogger.objects.all().count()
    num_posts = Post.objects.all().count()
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'= num_visits+1

    return render(
        request,
        'index.html',
        context={'num_bloggers': num_bloggers,
            'num_posts': num_posts,
            'num_visits': num_visits},
    )

from django.views import generic

class PostListView(generic.ListView):
    model = Post
    paginate_by = 10

class ThisPostView(generic.DetailView):
    model = Post

class BloggerListView(generic.ListView):
    model = Blogger

class AboutBloggerView(generic.DetailView):
    model = Blogger

from django.views.generic.edit import CreateView

class AddCommentView(CreateView):
    model = Post