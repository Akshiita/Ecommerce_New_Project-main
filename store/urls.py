from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='store'),
	path('contact',views.contact,name='contact'),
	path('faq/', views.faq, name='faq'),

    # path('contact/', contact_us, name='contact_us'),
    # path('contact/success/', views.contact_success, name='contact_success'),
	
	path('about',views.about,name='about'),
    path('category/<slug:category_slug>',views.store,name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/',views.product_detail,name='product_detail'),
    path('search/',views.search,name='search'),
]

