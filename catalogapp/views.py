from django.shortcuts import render



from .models import Product


from django.core.paginator import Paginator

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.


#Class-based views
class ProductListView(ListView):
    template_name = 'catalogapp/list.html'
    model = Product
    paginate_by = 24

    def get_queryset(self):
        return self.model.objects.all()[:100]
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        return context

class ProductDetailView(DetailView):
    template_name = 'catalogapp/item.html'
    model = Product



#Function-based views
def show_list(request):
    items = Product.objects.all()[:100]

    paginator = Paginator(items, 24)

    page_num = 1
    if 'page' in request.GET:
        page_num = request.GET['page']
    
    page = paginator.get_page(page_num)
    
    context = {
        'page_obj': page,
        }

    return render(request, 'catalogapp/list.html', context=context)

def show_item(request, pk):
    item = Product.objects.get(pk=pk)

    context = {
        'object': item,
        }

    return render(request, 'catalogapp/item.html', context=context)