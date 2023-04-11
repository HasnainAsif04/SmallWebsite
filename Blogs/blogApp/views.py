from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def index(request):
    blogs = BlogPost.objects.all()
    context = {'blogs':blogs}
    return render(request, 'index.html', context)

@login_required
def dashboard(request):
    user_blogs = BlogPost.objects.all().filter(user = request.user)
    # print(request.user.username)
    return render(request, 'dashboard.html', {'user_blogs':user_blogs})

def about_view(request):
    template = 'about.html'
    return render(request, template)

# def create_newpost(request):
#     form = BlogPostForm()
#     template = 'createpost.html'
#     return render(request, template, {"form":form})

from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import BlogPostForm

from django.contrib.auth.decorators import login_required

@login_required
def create_newpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.save()
            messages.success(request, 'Your post has been successfully created.')
            return redirect('/')
    else:
        form = BlogPostForm()
    template = 'createpost.html'
    context = {'form': form}
    return render(request, template, context)


