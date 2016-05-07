from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from .models import Product
from .models import Order
from .forms import ProductForm
from .forms import OrderForm


product_list = ListView.as_view(model=Product)

product_detail = DetailView.as_view(model=Product)

product_new = CreateView.as_view(model=Product, form_class=ProductForm)
    # success_url=reverse_lazy('shop:product_list'))

product_edit = UpdateView.as_view(model=Product, form_class=ProductForm)


# order_new = CreateView.as_view(model=Order, form_class=OrderForm)

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs['product_pk'])

        order = form.save(commit=False)
        order.product = product
        order.name = product.name
        order.amount = product.price
        order.save()
        return super(OrderCreateView, self).form_valid(form)

    def get_success_url(self):
        product_pk = self.kwargs['product_pk']
        order_pk = self.object.pk
        return reverse('shop:order_pay', args=[product_pk, order_pk])

order_new = OrderCreateView.as_view()


def order_pay(request, product_pk, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'shop/order_pay.html', {
        'order': order,
    })
