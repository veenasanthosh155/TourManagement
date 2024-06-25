from django.shortcuts import render
from tourapp.models import Package
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
@login_required
def search(request):
    query = ""
    b = None
    if (request.method == "POST"):
        query = request.POST['q']
        if (query):
            b = Package.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request, 'search.html', {'query': query, 'b': b})