
from django.shortcuts import render, redirect
from .forms import CompanyForm, SeparatorForm, EmployerForm, ProductForm, PlanForm
from django.contrib.auth.decorators import login_required
from src.models import Company, Separator, Employer, Carroussel, Plan, Product



#INFORMATION PAGES
def home(request):
    return render (request, "home.html")

def about(request):
    return render (request, "about.html")

def contact(request):
    return render (request, "contact.html")

def conditions(request):
    return render (request, "conditions.html")

#COMPANIES
@login_required
def listing_companies(request):
    companies = Company.objects.all()
    context = {
        "companies": companies,

    }
    return render (request, "list_companies.html", context)

@login_required
def retrieve_company(request, pk):
    company = Company.objects.get(id=pk)
    context={
        "company": company,
    }

    return render(request, "company.html", context)

@login_required
def company_create(request):
    form = CompanyForm()
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("/companies")
        
    context = {
        "form": form
    }
    return render (request, "company_create.html", context)

@login_required
def company_update(request, pk):
    company = Company.objects.get(id=pk)
    form = CompanyForm(instance=company)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect("/companies/")
        
    context = {
        "form": form
    }
    return render (request, "company_update.html", context)

@login_required
def company_delete(request, pk):
    company = Company.objects.get(id=pk)
    company.delete()
    return redirect("/companies/")

#SEPARATOR

@login_required
def listing_separator(request):
    company = Company.objects.get(user=request.user)
    separators = Separator.objects.filter(company=company)
    context = {
        "separators": separators,

    }
    return render (request, "list_separator.html", context)

@login_required
def retrieve_separator(request, pk):
    separator = Separator.objects.get(id=pk)
    context={
        "separator": separator,
    }

    return render(request, "separator.html", context)

@login_required
def separator_create(request):
    form = SeparatorForm()
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        form = SeparatorForm(request.POST )
        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = company
            instance.save()
            return redirect("/separators/")
        
    context = {
        "form": form
    }
    return render (request, "separator_create.html", context)

@login_required
def separator_update(request, pk):
    separator = Separator.objects.get(id=pk)
    form = SeparatorForm(instance=separator)
    if request.method == "POST":
        form = SeparatorForm(request.POST, instance=separator)
        if form.is_valid():
            form.save()
            return redirect("/separators/")
        
    context = {
        "form": form
    }
    return render (request, "separator_update.html", context)

@login_required
def separator_delete(request, pk):
    separator = Separator.objects.get(id=pk)
    separator.delete()
    return redirect("/separators/")

#EMPLOYERS

@login_required
def listing_employer(request):
    employers = Employer.objects.all()
    context = {
        "employers": employers,

    }
    return render (request, "list_employer.html", context)

@login_required
def retrieve_employer(request, pk):
    employer = Employer.objects.get(id=pk)
    context={
        "employer": employer,
    }

    return render(request, "employer.html", context)

@login_required
def add_employer(request):
    form = EmployerForm()
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        form = EmployerForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = company
            instance.save()
            return redirect("/employers/")
        
    context = {
        "form": form
    }
    return render (request, "add_employer.html", context)

@login_required
def employer_update(request, pk):
    employer = Employer.objects.get(id=pk)
    form = EmployerForm(instance=employer)
    if request.method == "POST":
        form = EmployerForm(request.POST, instance=employer)
        if form.is_valid():
            form.save()
            return redirect("/employers/")
        
    context = {
        "form": form
    }
    return render (request, "employer_update.html", context)

@login_required
def employer_delete(request, pk):
    employer = Employer.objects.get(id=pk)
    employer.delete()
    return redirect("/employers/")

#PRODUCTS

@login_required
def listing_product(request):
    products = Product.objects.all()
    context = {
        "products": products,

    }
    return render (request, "list_product.html", context)

@login_required
def retrieve_product(request, pk):
    product = Product.objects.get(id=pk)
    context={
        "product": product,
    }

    return render(request, "product.html", context)

@login_required
def add_product(request):
    form = ProductForm()
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = company
            instance.save()
            return redirect("/products/")
        
    context = {
        "form": form
    }
    return render (request, "add_product.html", context)

@login_required
def product_update(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("/products/")
        
    context = {
        "form": form
    }
    return render (request, "product_update.html", context)

@login_required
def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect("/products/")

#PLAN

@login_required
def listing_plan(request):
    plans = Plan.objects.all()
    context = {
        "plans": plans,

    }
    return render (request, "list_plan.html", context)

@login_required
def retrieve_plan(request, pk):
    plan = Plan.objects.get(id=pk)
    context={
        "plan": plan,
    }

    return render(request, "plan.html", context)

@login_required
def add_plan(request):
    form = PlanForm()
    company = Company.objects.get(user=request.user)
    if request.method == "POST":
        form = PlanForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.company = company
            instance.save()
            return redirect("/plans/")
        
    context = {
        "form": form
    }
    return render (request, "add_plan.html", context)

@login_required
def plan_update(request, pk):
    plan = Plan.objects.get(id=pk)
    form = PlanForm(instance=plan)
    if request.method == "POST":
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect("/plans/")
        
    context = {
        "form": form
    }
    return render (request, "plan_update.html", context)

@login_required
def plan_delete(request, pk):
    plan = Plan.objects.get(id=pk)
    plan.delete()
    return redirect("/plans/")







#WEBPAGE

def my_wiz_view(request, slug):
    company = Company.objects.get(slug=slug)
    separators = Separator.objects.filter(company=company)
    employers = Employer.objects.filter(company=company)
    carrousels = Carroussel.objects.filter(company=company)
    plans = Plan.objects.filter(company=company)
    products = Product.objects.filter(company=company)


    context = {
        "company": company,
        "separators": separators,
        "employers": employers,
        "carrousels": carrousels,
        "products": products,
        "plans": plans,
    }

    return render(request, "my_wiz_view.html", context)