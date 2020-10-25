from django.shortcuts import render

# Create your views here. Extra comment
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def html_mock(request):
    return render(request, 'blog/html_mock.html', {})

def html_mock2(request):
    return render(request, 'blog/html_mock2.html', {})
