from django.urls import path
from django.conf import settings
from django.conf.urls.static import static  

from .views import index , products_page ,LaptopListView , ComputerListView , GameConsoleListView

urlpatterns = [
    path("" , index , name="home-page") , 

    path("products/laptop/", LaptopListView.as_view(), name="laptop-list"),
    path("products/computer/", ComputerListView.as_view(), name="computer-list"),
    path("products/gameconsole/", GameConsoleListView.as_view(), name="gamec-list"),

    path("products/", products_page, name="product-list"),
    path("products/<slug:product_slug>/", products_page , name="product-detail"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
     
 
        