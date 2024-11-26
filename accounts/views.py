from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')


# from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {'user': request.user})


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def employee_list_view(request):
    return render(request, 'employee_list.html')


from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')



from django.shortcuts import render, redirect
from .forms import EmployeeForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee  # Assuming you have an Employee model
from .forms import EmployeeForm  # If you are using Django forms

# View to create a new employee
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee  # Assuming you have an Employee model

# Renamed function to match the URL
# accounts/views.py
from django.shortcuts import render, redirect
from .models import Employee

def create_employee(request):
    if request.method == 'POST':
        # Collect data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        designation = request.POST.get('designation')
        gender = request.POST.get('gender')
        course = request.POST.getlist('course')  # Multiple checkboxes
        img_upload = request.FILES.get('img_upload')  # File upload

        # Create a new Employee object
        employee = Employee(
            name=name,
            email=email,
            mobile=mobile,
            designation=designation,
            gender=gender,
            img_upload=img_upload,
        )
        employee.save()

        # Redirect to the employee list page (or wherever you need)
        return redirect('employee_list')  # Replace 'employee_list' with your actual URL name

    # If it's a GET request, display the form
    return render(request, 'create_employee.html')



from django.shortcuts import render
from .models import Employee

def employee_list_view(request):
    employees = Employee.objects.all()  # Fetch all employee records
    return render(request, 'employee_list.html', {'employees': employees})



from django.shortcuts import get_object_or_404

def employee_detail_view(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employee_detail.html', {'employee': employee})





from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeEditForm

def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeEditForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard or wherever you want after save
    else:
        form = EmployeeEditForm(instance=employee)

    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})






from django.http import HttpResponseRedirect

def employee_delete_view(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully!')
        return redirect('employee_list')  # Redirect to employee list
    return render(request, 'employee_confirm_delete.html', {'employee': employee})



from django.shortcuts import render, redirect
from .forms import EmployeeForm

def create_employee_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save(commit=False)
            # Save courses as a comma-separated string
            employee.courses = ','.join(form.cleaned_data['courses'])
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'create_employee.html', {'form': form})




def success_view(request):
    return render(request, 'success.html')


from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeEditForm

# Edit Employee View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeEditForm

# Edit Employee View
from django.shortcuts import get_object_or_404

def employee_edit_view(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.courses = ','.join(form.cleaned_data['courses'])
            employee.save()
            return redirect('employee_list')
    else:
        initial_data = {
            'courses': employee.courses.split(',')  # Populate checkboxes with current selections
        }
        form = EmployeeForm(instance=employee, initial=initial_data)

    return render(request, 'edit_employee.html', {'form': form})



