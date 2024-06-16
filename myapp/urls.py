
from django.urls import path
from . import views


urlpatterns = [
    path('',views.login_user,name='login'),
    path('register/',views.register_user,name='register'),
    path('create/',views.createbook,name="createbook"),
    path('author/',views.create_author,name="author"),
    path('list/',views.listBook,name="booklist"),
    path('details/<int:book_id>/',views.detailsBook,name="details"),
    path('update/<int:book_id>/',views.updateBook,name="update"),
    path('delete/<int:book_id>/',views.deleteBook,name="delete"),
    path('search/',views.searchbook,name="search"),


]