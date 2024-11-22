from django.shortcuts import render

# Create your views here.
def post _list(request):
    return render(request, 'blog/post_list.html',{})