from django.shortcuts import render
from .models import Post
from django.utils import timezone


# Create your views here.

# Create your views here
#
def post_list(request):
<<<<<<< HEAD
     return render(request, 'blog/post_list.html', {})
=======
     posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
     return render(request, 'blog/post_list.html', {'posts':posts})
>>>>>>> f4da04642f4a80f03f0b3c2985c655d587ddf4e2

