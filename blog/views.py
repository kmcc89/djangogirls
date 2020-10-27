from django.shortcuts import render
from .models import Post
from django.utils import timezone   

#A view is a place where we put the "logic" of our application.
#It requests information from our models 

# Create your views here. Extra comment

#function takes a request and returns the value of calling render function 
# then looks for a html template file in the blog app
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def html_mock(request):
    return render(request, 'blog/html_mock.html', {})

def html_mock2(request):
    return render(request, 'blog/html_mock2.html', {})
