from django.urls import path
from . import views 

app_name='members'
urlpatterns = [
    path('members/', views.members, name='members'),
    path('hello/', views.hello, name='hello'),
    path('name/', views.name ,name='name'),
    path('members/details/<int:id>', views.details, name='details'),
    path('', views.main, name='main'),
    path('testing/', views.testing ,name='testing'),
    path('greeting/', views.greeting ,name='greeting'),
    #fetching the data from the database in the table format...
    path('table/', views.table,name="table"),


    #crud operations using django...
    path('list/', views.employees_list, name='employees-list'),
    path('create/', views.create_employee, name='create-employee'),
    path('edit/<str:pk>/', views.edit_employee, name='edit-employee'),
    path('delete/<str:pk>/', views.delete_employee, name='delete-employee'),
    path('searchbar/',views.searchbar, name='searchbar'),

    # login and logout pages and register...
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),

    # import view
    path('import/', views.import_excel,name='import'),
    path('stage/', views.stage, name='stage'),
    path('export/', views.export_csv,name='exportcsv'),
    
    ##pdf convertion
    path('showmembers/', views.show_members,name='showmembers'),
    path('createpdf/', views.pdf_create,name='createpdf'),

    #templates..
    path('template/', views.bootstrap,name='template'),

    #portfolio
    path('portfolio/', views.portfolio,name='port-folio'),

    #admin page..
    path('adminpage/', views.admin,name='admin'),



    


    ]
