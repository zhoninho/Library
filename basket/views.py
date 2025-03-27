from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic


# def add_product(request):
#     if request.method == 'POST':
#         form = forms.ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('products_list')
#     else:
#         form = forms.ProductForm()
#     return render(
#         request,
#         template_name='basket/add_product.html',
#         context={'form': form},
#     )


class AddProductView(generic.CreateView):
    template_name = 'basket/add_product.html'
    form_class = forms.ProductForm
    success_url = "/products_list/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(AddProductView, self).form_valid(form=form)

class SearchProductsView(generic.ListView):
    template_name = 'basket/products_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return models.ProductList.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

# read list/detail
# def products_list(request):
#     if request.method == 'GET':
#         query = models.ProductList.objects.all().order_by('-id')
#         return render(
#             request,
#             template_name='basket/products_list.html',
#             context={'products': query},
#         )

class ProductsListView(generic.ListView):
    template_name = 'basket/products_list.html'
    context_object_name = 'products'
    model = models.ProductList

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


# def product_detail(request, id):
#     if request.method == 'GET':
#         product_id = get_object_or_404(models.ProductList, id=id)
#         return render(
#             request,
#             template_name='basket/product_detail.html',
#             context={'product_id': product_id}
#         )

class ProductDetailView(generic.DetailView):
    template_name = 'basket/product_detail.html'
    context_object_name = 'product_id'

    def get_object(self,*args, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.ProductList, id=product_id)



# Update
# def update_product(request, id):
#     product_id = get_object_or_404(models.ProductList, id=id)
#     if request.method == 'POST':
#         form = forms.ProductForm(request.POST, instance=product_id)
#         if form.is_valid():
#             form.save()
#             return redirect('products_list')
#     else:
#         form = forms.ProductForm(instance=product_id)
#
#     return render(
#         request,
#         template_name='Basket/update_product.html',
#         context={
#             'form': form,
#             'product_id': product_id
#         }
#     )

class UpdateProductView(generic.UpdateView):
    template_name = 'basket/update_product.html'
    form_class = forms.ProductForm
    success_url = '/products_list/'

    def get_object(self,*args, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.ProductList,id=product_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateProductView, self).form_valid(form=form)


# def delete_product(request, id):
#     task_id = get_object_or_404(models.ProductList, id=id)
#     task_id.delete()
#     return redirect('products_list')

class DeleteProductView(generic.DeleteView):
    template_name = 'basket/confirm_delete.html'
    success_url = '/products_list/'

    def get_object(self,*args, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.ProductList,id=product_id)