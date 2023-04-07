from django import urls
from django.urls import path

from . import views
from .views import BookListView, BookDetailView, BookCheckoutView, SearchResultsView, HomePageView, MyProfileView, \
    toggle_favorite, MyProfileCreate, MyProfileUpdate, cart, add_to_cart, remove_from_cart, OrderListView, \
    book_recommendations

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('add_favorite/<int:book_id>/', toggle_favorite, name='toggle_favorite'),

    path('myprofile/', MyProfileView.as_view(), name='myprofile'),
    path('createprofile/', MyProfileCreate.as_view(), name='createprofile'),
    path('editprofile/', MyProfileUpdate.as_view(), name='editprofile'),

    path('cart/', cart, name='mycart'),
    path('cart/add/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:book_id>/', remove_from_cart, name='remove_from_cart'),

    path('book_list', BookListView.as_view(), name='list'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail-view'),
    path('checkout/<int:pk>/', BookCheckoutView.as_view(), name='checkout'),
    path('complete', views.PaymentComplete, name='complete'),
    path('book-recommendations/<str:query>/', book_recommendations, name='book_recommendations'),
    path('search', SearchResultsView.as_view(), name='search'),
    path('orders/', OrderListView.as_view(), name='orders')

]
