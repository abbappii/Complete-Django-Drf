import imp
from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateAPIVIEW.as_view()),
    path('<int:pk>/delete/', views.ProductDeleteAPIVIEW.as_view()),


    path('<int:pk>/', views.ProductDetailAPIVIEW.as_view()),

]