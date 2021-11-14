from django.shortcuts import render
from .models import Collection
from django.db.models import Count


# Create your views here.
def index(request):
    collections = Collection.objects.all().values('collection_time').annotate(collection_frequency=Count("bin_id"))
    print('collections', collections)
    return render(request, "index.html", {"collections": collections})

