
from django.contrib import admin
from django.urls import path, include
from src.views import (listing_companies, 
                        list_all_companies,
                        retrieve_company, 
                        company_create, 
                        company_update,
                        company_delete,
                        listing_separator,
                        retrieve_separator,
                        separator_create,
                        separator_update,
                        separator_delete,
                        employer_update,
                        employer_delete,
                        listing_employer,
                        retrieve_employer,
                        add_employer, 
                        add_product,
                        product_update,
                        product_delete,
                        retrieve_product,
                        listing_product,
                        add_plan,
                        plan_update,
                        plan_delete,
                        listing_plan,
                        retrieve_plan,
                        home, 
                        about, 
                        contact, 
                        conditions, 
                        my_wiz_view)

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),


    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('conditions/', conditions),


    path('companies/', listing_companies),
    path('all_companies/', list_all_companies),
    path('companies/<pk>/', retrieve_company),
    path('companies-create', company_create, name="create-company"),
    path('companies/<pk>/update/', company_update),
    path('companies/<pk>/delete/', company_delete),

    
    path('separators/', listing_separator),
    path('separators/<pk>/', retrieve_separator),
    path('separators-create/', separator_create, name="create-separator"),
    path('separators/<pk>/update/', separator_update, name="update-separator"),
    path('separators/<pk>/delete/', separator_delete),


    path('plans/', listing_plan),
    path('plans/<pk>/', retrieve_plan),
    path('plans-create/', add_plan, name="create-plan"),
    path('plans/<pk>/update/', plan_update),
    path('plans/<pk>/delete/', plan_delete),


    path('employers/', listing_employer),
    path('employers/<pk>/', retrieve_employer),
    path('employers-create/', add_employer, name="create-employer"),
    path('employers/<pk>/update/', employer_update),
    path('employers/<pk>/delete/', employer_delete),

    path('products/', listing_product),
    path('products/<pk>/', retrieve_product),
    path('products-create/', add_product, name="create-product"),
    path('products/<pk>/update/', product_update),
    path('products/<pk>/delete/', product_delete),




    path('<slug:slug>/', my_wiz_view),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)