from django.urls import path
import main.views as views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create-product', views.create_product, name='create_product'),
    path('xml/', views.show_xml, name='show_xml'), 
    path('json/', views.show_json, name='show_json'), 
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('plus_product_amount/<int:id>', views.plus_product_amount, name='plus_product_amount'),
    path('minus_product_amount/<int:id>', views.minus_product_amount, name='minus_product_amount'),
    path('remove_product/<int:id>', views.remove_product, name='remove_product'),
    path('edit-product/<int:id>', views.edit_product, name='edit_product'),
    path('get-product/', views.get_product_json, name='get_product_json'),
    path('create-product-ajax/', views.add_product_ajax, name='add_product_ajax')
]