from django.forms import ModelForm
from .models import Company, Employer, Separator, Carroussel, Plan, Product


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = [
            "company",
            "desc",
            "image",
            "about",
            "cell",
            "address",
            "email",
            "slug",
            "logo",
            "welcome",
        ]

class SeparatorForm(ModelForm):
    class Meta:
        model = Separator
        fields = [
            "title",
            "desc",
            "image",
            "place",
        ]


class CarrousselForm(ModelForm):
    class Meta:
        model = Carroussel
        fields = [
            "company",
            "title",
            "background",
            "desc",
        ]


class EmployerForm(ModelForm):
    class Meta:
        model = Employer
        fields = [
                "name",
                "funcion",
                "image",
                "facebook",
                "instagram"
            ]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
                "image",
                "price",
                "desc",
            ]


class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = [
                "title",
                "price",
                "desc",
            ]



