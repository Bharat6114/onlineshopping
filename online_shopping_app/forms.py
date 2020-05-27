from django import forms
from online_shopping_app.models import Products 
from online_shopping_app.models import Category


class ProductsCreateForm(forms.ModelForm):
    CATEGORY_CHOICES = [(category.id, category.title) for category in Category.objects.all()]
    category = forms.MultipleChoiceField(
        required=True, widget=forms.CheckboxSelectMultiple, choices=CATEGORY_CHOICES,
    )

    class Meta:
        model = Products
        fields = "product_name", "product_description", "cover_image1","cover_image2","cover_image3", "category"