from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
from .models import Motto, Video, Gadget, Review, Category

class HomeView(TemplateView):
    template_name = 'shop/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['motto'] = Motto.objects.first()
        context['video'] = Video.objects.first()
        context['top_gadgets'] = Gadget.objects.order_by('-popularity')[:5]
        return context

class ProductListView(ListView):
    model = Gadget
    template_name = 'shop/product_list.html'
    context_object_name = 'gadgets'

    def get_queryset(self):
        category_name = self.kwargs.get('category')
        if category_name:
            category = get_object_or_404(Category, name=category_name)
            return Gadget.objects.filter(categories=category)
        return Gadget.objects.all()

class ProductDetailView(DetailView):
    model = Gadget
    template_name = 'shop/product_detail.html'
    context_object_name = 'gadget'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()
        return context

class AddReviewView(TemplateView):
    template_name = 'shop/add_review.html'

    def post(self, request, *args, **kwargs):
        gadget = get_object_or_404(Gadget, pk=self.kwargs['pk'])
        author = request.POST.get('author')
        text = request.POST.get('text')
        Review.objects.create(gadget=gadget, author=author, text=text)
        return redirect('product_detail', pk=gadget.pk)
