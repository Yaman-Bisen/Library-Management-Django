from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('',views.home),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('admindashboard/',views.adminDashboard, name='admindashboard'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    path('viewBooks/',views.viewBooks, name="viewbooks"),
    path('addBook/',views.addBook, name="addbook"),
    path('updateBook/',views.updateBook, name="updatebook"),
    path('updateBookDetail/<int:id>/',views.updateBookDetail, name="updatebookdetail"),
    path('deleteBook/',views.deleteBook, name="deletebook"),
    path('deleteBookDetail/<int:id>/',views.deleteBookDetail, name="deletebookdetail"),
]
