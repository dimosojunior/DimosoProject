from django.urls import path
from .import views



urlpatterns = [

   
    


    path('Documents/', views.Documents, name="Documents"),
    path('<slug:mydocumentstype_slug>/', views.Documents, name="documents_by_category"),

    path('search_mydocuments', views.search_mydocuments, name="search_mydocuments"),

    #hii ni kwa ajili ya autocomplete
    path('search_mydocument', views.search_mydocument, name="search_mydocument"),
    path('upload_mydocuments', views.upload_mydocuments, name="upload_mydocuments"),


    #path('base/', views.base, name="base"),
       
 
]