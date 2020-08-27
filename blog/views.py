from django.shortcuts import render

# Create your views here. Extra comment
def post_list(request):
    return render(request, 'blog/post_list.html', {})
