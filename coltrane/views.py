#from django.shortcuts import render_to_response, get_object_or_404
from coltrane.models import Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from taggit.models import Tag

# def entry_index(request):
#     return render_to_response("coltrane/entry_index.html", {'entry_list': Entry.objects.all()})
#
# def entry_detail(request, year, month, day, slug):
#     import datetime, time
#     date_stamp = time.strptime(year+month+day, "%Y%m%d")
#     pub_date = datetime.date(*date_stamp[:3])
#     entry = get_object_or_404(Entry, pub_date__year=pub_date.year,
#                                      pub_date__month=pub_date.month,
#                                      pub_date__day=pub_date.day,
#                                      slug=slug)
#     return render_to_response("coltrane/entry_detail.html",
#         {'entry' : entry})
#def category_list(request):
#    return render_to_response("coltrane/category_list.html",
#        {'object_list': Category.objects.all()})
class CategoryDetailView(DetailView):
    model = Category

class CategoryListView(ListView):
    model = Category

class TagListView(ListView):
    model = Tag

# def category_detail(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     return render_to_response("coltrane/category_detail.html", {'category': category})