from django.shortcuts import render
from .models import GrassDB

# Create your views here.


def post_list(request):

    Posts = GrassDB.objects.all()
    query = request.GET.get("query")
    post_data = GrassDB.objects.filter(Common_N=query)

    return_source = {'query': query, 'Posts': Posts, 'post_data': post_data}

    return render(request, 'post_list.html', return_source)
