from . import  views

from django.urls import path

app_name = 'store'

urlpatterns = [
    path('', views.home, name="home"),
    path('reports/', views.reports, name="reports"),
    path('products/clients/', views.clients, name="clients"),
    path('products/clients/<pk>/cdetails/', views.client_details, name="show-client"),
    path('products/', views.all_products, name="all_products"),
    
    path('products/<str:slug>/details/', views.product_details, name="product_details"),
    path('products/<pk>/delete/', views.delete_product, name="delete_product"),
    path('clients/<pk>/delete/', views.delete_client, name="delete_client"),
    path('products/add-new-product/', views.add_product, name="add_product"),
    path('products/<str:slug>/edit/', views.edit_product, name="edit_product"),
    path('products/line-form/', views.create_line_form, name="line-form"),
    path('products/line-detail/<pk>/', views.detail_line, name="detail-line"),
    path('products/bill/line/delete/', views.delete_line , name="delete-line"),
    path('products/bill/line/<pk>/update/', views.update_line_form , name="update-line"),
    path('products/bill/<pk>/', views.create_line, name="create-line"),
    
    path('products/bill/<int:id>/generate-bill/', views.generate_bill, name="generate_bill"),
    path('products/end-bill/', views.end_bill, name="end_bill"),
    
    path('products/bill/client/<pk>/detail/', views.detail_client, name="detail-client"),
    path('products/bill/<pk>/edit/', views.edit_bill_user_information, name="user-bill-form"),
    path('products/another-bill/<pk>/', views.another_bill_for_client, name="another-bill"),
    path('products/bill/<pk>/delete/', views.delete_bill, name="delete-bill"),
    path('add-new-bill/', views.add_bill, name="add-bill"),
    path('products/bills/', views.bills, name="bills"),
    path('products/bill/<pk>/complete/', views.complete_bill, name="complete-bill"),
    path('products/bill/<pk>/details/', views.bill_details, name="bill_details"),
    path('products/line-message/', views.line_message, name="message"),
    path('autosearch/products/',views.autoSearch_products , name='autosearch'),
    path('autosearch/bills/',views.autosearch_bills , name='autosearch_bills'),
    path('autosearch/clients/',views.autosearch_clients , name='autosearch_clients'),
    path('ajax_live_bill_user_update/',views.live_bill_user_update , name='live_bill_user_update'),
    path('ajax_payment/',views.payment , name='payment'),
    
    # quiq bill urls
    path('products/quiqbill/<pk>/', views.create_quiqline, name="create_quiqline"),
    path('products/quiqline-detail/<pk>/', views.detail_quiqline, name="detail_quiqline"),
    path('products/quiqline-form/', views.create_quiqline_form, name="quiqline_form"),
    path('products/bill/quiqline/<pk>/update/', views.update_quiqline , name="update_quiqline"),
    path('products/quiqbills/', views.quiq_bills, name="quiqbills"),
    path('products/quiqbill/quiqline/delete/', views.delete_quiqline , name="delete_quiqline"),
    path('ajax_quiqbill_payment/',views.quiqbill_payment , name='quiqbill_payment'),
    path('quiqbill/<pk>/delete/',views.delete_quiqbill , name='delete_quiqbill'),
    path('products/add-new/quiqbill/',views.add_quiqbill , name='add_quiqbill'),
    path('products/quiqbill/<pk>/print/',views.print_quiqbill , name='print_quiqbill'),
    path('ajax_live_quiqbill/',views.live_quiqbill , name='live_quiqbill'),
    path('autosearch/quiqbills/',views.autosearch_quiqbills , name='autosearch_quiqbills'),

]
