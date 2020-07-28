from django.shortcuts import render
from .models import CommentDB

# Create your views here.


def index(request):
    post_data = CommentDB.objects.filter(username='biezz21')
    return render(request, 'index.html', {'post_data': post_data})
