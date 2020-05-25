from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from online_shopping_app.models import Category
from online_shopping_app.models import Products
from django.views import View
from django.views.generic import (
    TemplateView,
    DeleteView,
    UpdateView,
    CreateView,
    ListView,
    DetailView,
)


# Create your views here.
class CategoryProductsView(View):
    def get(self, request, category_id, *args, **kwargs):
        template_name = "Products/categories.html"
        # category = Category.objects.get(pk=category_id)
        category = get_object_or_404(Category, pk=category_id)
        category_Products_list = Products.objects.filter(category=category)
        return render(
            request, template_name, {"category_Products_list": category_Products_list, "category": category}
        )


# class CategoryProductsView(ListView):
#     model = Products
#     context_object_name = "category_Products_list"
#     template_name = "Products/categories.html"

#     # queryset = Products.objects.all()

#     def get_queryset(self):
#         print("KWARGS: ", self.kwargs)
#         category_id = self.kwargs["category_id"]
#         category = get_object_or_404(Category, id=category_id)
#         return Products.objects.filter(category=category)


class ProductsTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        print(categories)
        category_Products_list = {}
        for category in categories:
            # context[category.title] = Products.objects.filter(category=category)
            category_Products_list[category] = Products.objects.filter(category=category)
        context["products_list"] = Products.objects.all().order_by("-created_at")[:4]
        context["trending_products"] = Products.objects.order_by("-count")
        context["category_products_list"] = category_Products_list
        print(context)
        return context

class ProductsDetail(DetailView):
    model = Products
    template_name = "products/single_Products.html"
    context_object_name = "detail_products"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.count = self.object.count + 1
        self.object.save()
        context["popular_products"] = Products.objects.order_by("-count")[:4]
        return context