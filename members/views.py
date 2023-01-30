from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Employee
from .forms import EmployeeForm, CreateUserForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
from .filters import EmployeeFilter
from django.contrib.auth.forms import UserCreationForm 
from .models import Person
from .resources import PersonResource
from django.contrib import messages
from tablib import Dataset
import csv
#pdf imports..
from django.http import FileResponse
import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



from django.contrib.auth import authenticate, login, logout

from django.contrib import messages #it used to give the flash messages..
#decorators..
from django.contrib.auth.decorators import login_required 

# from django.shortcuts import render, redirect
# from .models import Employee
# from .forms import EmployeeForm

# Create your views here.
def members(request):
  mymembers = Member.objects.all().values() #this code will fetch the data from the database
  template = loader.get_template('data.html') #This code will display the fetched data using the html
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('fulldetails.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


#main page or index page
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())    

def hello(request):
    return HttpResponse("Hello this is swamy")
def name(request):
    return HttpResponse("Hello my name is swamypatel")


def testing(request):
    template = loader.get_template('testing.html')
    context ={
        'Name' : "swamy",
        'Role' : "Python developer",
        'package' : "3LPA",
        'age':'21',
    }
    return HttpResponse(template.render(context,request))
# def greeting(request):
#     template = loader.get_template('dr.html')
#     context={
#         'greeting':1,
#         'name':"swamy",
#     }
#     return HttpResponse(template.render(context,request))
def greeting(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'members': mymembers,
  }
  return HttpResponse(template.render(context, request))

##fetching the data from the database..
def table(request):
    #mymembers = Member.objects.order_by('firstname').values() #it is used to fetch the data in the asc order
    # mymembers = Member.objects.filter(firstname='Gouthami').values() #it used to filter the data and fetches 1stname
    # mymembers = Member.objects.order_by('-firstname').values() #it fetches the data in the descending order..
    mymembers = Member.objects.all().values()

    template = loader.get_template('table.html')
    context={
        'member':mymembers,
    }
    return HttpResponse(template.render(context,request))

 # crud operations in the django
def employees_list(request):
  employees = Employee.objects.all()
  page = Paginator(employees, 3 )
  page_list = request.GET.get('page') #the code is not clear..
  page = page.get_page(page_list)

  myfilter = EmployeeFilter(request.GET, queryset=employees)
  employees = myfilter.qs
  context = {
    'page':page,
    'myfilter':myfilter,
  }
  return render(request, 'employee/list.html', context)

def create_employee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('members:employees-list')

    context = {
        'form': form,
    }
    return render(request, 'employee/create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('members:employees-list')

    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'employee/edit.html', context)
    #first  it goes to the edit form and it checks to the method is post or not if it is then it checks the form is valid or not after that is saves...


def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('members:employees-list')

    context = {
        'employee': employee,
    }
    return render(request, 'employee/delete.html', context)
#search view....
def searchbar(request):
  if request.method == 'GET':
    search = request.GET.get('search')
    post =Employee.objects.all().filter(name=search)
    context = {
      'post':post
    }
    return render(request, 'searchbar.html',context)


#login
#logout
#Register 
#User authentication system...
def register(request):
  form = CreateUserForm()

  if request.method == 'POST':
    form = CreateUserForm(request.POST) #it  is used to create the default django form in django
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      messages.success(request, "Account was created for" +" " + user)

      return redirect('members:login')
  context = {
    'form':form,
  }
  return render(request, 'register.html', context)
  
def loginpage(request):

  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')  

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request,user)
      return redirect('members:employees-list')  #if we want to redirect any page to another we use the namespace and name of the view...
    else:
      messages.info(request, 'Username OR  Password is not correct')

  context = {}
  return render(request, 'login.html', context)

def logoutpage(request):
  logout(request)
  return redirect('members:login')



#import function...
def import_excel(request):
  if request.method == 'POST':
    person_resource = PersonResource()
    dataset  = Dataset()
    new_person = request.FILES['myfile']
    
    if not new_person.name.endswith('csv'):
      messages.info(request,'Wrong format')
      return render(request,'upload.html')
    
    imported_data = dataset.load(new_person.read().decode("utf-8"),format='csv')
    for data in imported_data:
      value = Person(
        data[0],
        data[1],
      )
      value.save()
  return render(request,'upload.html')

#Export function .... Exporting the data from the DB to the Csv file..

def stage(request):
    slist = Employee.objects.all()
    return render(request, {'slist': slist})

def export_csv(request):  
    response = HttpResponse(content_type='text/csv')  #it is for the response is getting as csv/text
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  #it saves the all data in the file.csv
    employees = Employee.objects.all()

    writer = csv.writer(response)
    writer.writerow(['NAME','EMAIL','CONTACT','ROLE','SALARY']) #col names  for the csv file 


    for employee in employees:  
        writer.writerow([employee.name,employee.email,employee.contact,employee.role,employee.salary,employee.id]) #it joining rows and employee vars or it joining col name and fetched data makes csv file. 
    return response 

def show_members(request):
  members = Employee.objects.all()

  context = {
    'members':members
  }
  return render(request,'pdftemp.html',context)

def pdf_create(request):
  members =Employee.objects.all()

  template_path = 'pdfreport.html'

  context = {'members':members}

  response = HttpResponse(content_type='application/pdf')

  response['Content-Disposition'] = 'filename = "report.pdf"'

  template = get_template(template_path)

  html = template.render(context)

  #create a pdf
  pisa_status = pisa.CreatePDF(
    html, dest=response )
  #if error then show some message..
  if pisa_status.err:
    return HttpResponse('we had some errors')
  return response

def bootstrap(request):
  return render(request,'index.html')

#portfolio resume website..

def portfolio(request):
  return render(request,'portfolio/home.html')

#admin page..
def admin(request):
  return render(request,'adminpage/admin.html')
  

  