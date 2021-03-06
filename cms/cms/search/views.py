from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage
from django.http import HttpResponseRedirect

# Create your views here.
def search(request):
    query = request.GET.get('q', '')
    results = []
    keyword_results = []

    if query:
        keyword_results = FlatPage.objects.filter(searchkeyword__keyword__in = query.split()).distinct()
        results = FlatPage.objects.filter(content__icontains=query)

        if (keyword_results.count() == 1):
            return HttpResponseRedirect(keyword_results[0].get_absolute_url())
    return render_to_response("search/search.html",
                              {'query' : query, 'keyword_results' : keyword_results, 'results' : results})